# pylint: disable=unused-import
import pytest
import tests.helpers.constants as constants
from geckordp.rdp_client import RDPClient
from geckordp.actors.root import RootActor
from geckordp.actors.descriptors.tab import TabActor
from geckordp.actors.node import NodeActor
from geckordp.actors.inspector import InspectorActor
from geckordp.actors.walker import WalkerActor
from geckordp.logger import log, logdict


def init():
    cl = RDPClient(3)
    cl.connect(constants.REMOTE_HOST, constants.REMOTE_PORT)
    root = RootActor(cl)
    current_tab = root.current_tab()
    tab = TabActor(cl, current_tab["actor"])
    actor_ids = tab.get_target()
    inspector = InspectorActor(cl, actor_ids["inspectorActor"])
    walker = WalkerActor(cl, inspector.get_walker()["actor"])
    doc = walker.document()
    node = walker.query_selector(doc["actor"], "body h1")["node"]
    node = NodeActor(cl, node["actor"])
    return cl, node


def test_get_node_value():
    cl = None
    try:
        cl, node = init()
        val = node.get_node_value()
        log(val)
    finally:
        cl.disconnect()


def test_set_node_value():
    cl = None
    try:
        cl, node = init()
        val = node.set_node_value("")
        assert "domnode" in val["from"]
    finally:
        cl.disconnect()


def test_get_unique_selector():
    cl = None
    try:
        cl, node = init()
        val = node.get_unique_selector()
        assert isinstance(val, str)
        assert len(val) > 5
    finally:
        cl.disconnect()


def test_get_all_selectors():
    cl = None
    try:
        cl, node = init()
        val = node.get_all_selectors()
        assert isinstance(val, list)
        assert len(val) > 0
        assert len(val[0]) > 5
    finally:
        cl.disconnect()


def test_get_css_path():
    cl = None
    try:
        cl, node = init()
        val = node.get_css_path()
        assert isinstance(val, str)
        assert len(val) > 5
    finally:
        cl.disconnect()


def test_get_x_path():
    cl = None
    try:
        cl, node = init()
        val = node.get_x_path()
        assert isinstance(val, str)
        assert len(val) > 5
    finally:
        cl.disconnect()


def test_scroll_into_view():
    cl = None
    try:
        cl, node = init()
        val = node.scroll_into_view()
        assert "domnode" in val["from"]
    finally:
        cl.disconnect()


def test_get_image_data():
    cl = None
    try:
        cl, node = init()
        val = node.get_image_data()
        assert "domnode" in val["from"]
    finally:
        cl.disconnect()


def test_get_event_listener_info():
    cl = None
    try:
        cl, node = init()
        val = node.get_event_listener_info()
        assert isinstance(val, list)
    finally:
        cl.disconnect()


def test_modify_attributes():
    cl = None
    try:
        cl, node = init()
        val = node.modify_attributes([])
        assert "domnode" in val["from"]
    finally:
        cl.disconnect()


def test_get_font_family_data_url():
    cl = None
    try:
        cl, node = init()
        val = node.get_font_family_data_url("arial")
        assert val.get("data", None) != None
        assert val.get("size", None) != None
    finally:
        cl.disconnect()


def test_get_closest_background_color():
    cl = None
    try:
        cl, node = init()
        val = node.get_closest_background_color()
        assert isinstance(val, str)
        assert len(val) > 5
    finally:
        cl.disconnect()


def test_get_background_color():
    cl = None
    try:
        cl, node = init()
        val = node.get_background_color()
        assert isinstance(val, list)
        assert len(val) > 2
    finally:
        cl.disconnect()


def test_get_owner_global_dimensions():
    cl = None
    try:
        cl, node = init()
        val = node.get_owner_global_dimensions()
        assert val.get("innerWidth", None) != None
    finally:
        cl.disconnect()


# "Spec for 'domnode' specifies a 'connectToRemoteFrame' method that isn't implemented by the actor"
""" def test_connect_to_remote_frame():
    cl = None
    try:
        cl, node = init()
        val = node.connect_to_remote_frame()
        log(val)
    finally:
        cl.disconnect() """


def test_wait_for_frame_load():
    cl = None
    try:
        cl, node = init()
        val = node.wait_for_frame_load()
        assert "domnode" in val["from"]
    finally:
        cl.disconnect()