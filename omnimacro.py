#!/usr/bin/env python

"""Globally log the keys of keyboard input until a certain kombination and write
the sequence of keystrokes to a file.

author: andreasl
"""
import argparse

import enum
import pathlib
import pickle
from typing import List, Tuple

import pynput

Key = pynput.keyboard.Key
KeyCode = pynput.keyboard.KeyCode
KeyboardListener = pynput.keyboard.Listener


def parse_cmd_args() -> argparse.Namespace:
    """Parse the command line arguments and return the according namespace."""
    omnimacro_description = "omnimacro v.0.1.0"
    parser = argparse.ArgumentParser(description=omnimacro_description)
    parser.add_argument(
        "path",
        default=pathlib.Path.home() / ".omnimacro",
        nargs="?",
        help="path to a file from or to which to read the keystrokes",
        type=pathlib.Path,
    )
    parser.add_argument(
        "-p",
        "--play",
        action="store_true",
        default=False,
        help="Instead of writing a key sequence to a file, load the file and emulate"
        "the containing key sequence",
    )

    return parser.parse_args()


class KeyEventType(enum.Enum):
    """Specify the type of a keyboard event."""

    PRESS = enum.auto()
    RELEASE = enum.auto()


class State:
    """Represents the state of a macro recording session."""

    is_cmd_pressed: bool = False
    is_p_pressed: bool = False

    @staticmethod
    def update(key: Key, event_type: KeyEventType) -> bool:
        """Update the state and return whether the recording session should continue."""
        if key == Key.cmd and event_type == KeyEventType.PRESS:
            State.is_cmd_pressed = True
        elif key == Key.cmd and event_type == KeyEventType.RELEASE:
            State.is_cmd_pressed = False
        elif key == KeyCode.from_char("p") and event_type == KeyEventType.PRESS:
            State.is_p_pressed = True
        elif key == KeyCode.from_char("p") and event_type == KeyEventType.RELEASE:
            State.is_p_pressed = False

        return State.is_cmd_pressed and State.is_p_pressed


RECORDED_KEY_EVENTS: List[Tuple[int, KeyEventType]] = []


def on_press(key: Key):
    """Add key strokes to a list."""
    if State.update(key, KeyEventType.PRESS):
        return False
    if key != Key.cmd:
        RECORDED_KEY_EVENTS.append((key, KeyEventType.PRESS))
    return True


def on_release(key: Key):
    """Add key-release events to a list."""
    State.update(key, KeyEventType.RELEASE)
    if key != Key.cmd:
        RECORDED_KEY_EVENTS.append((key, KeyEventType.RELEASE))


def log_key_events(path: pathlib.Path):
    """Log keyboard events to a file."""
    with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    with open(path, "wb") as file:
        pickle.dump(RECORDED_KEY_EVENTS, file)


def play_key_events(path: pathlib.Path):
    """Play keyboard events from a pickle file."""
    with open(path, "rb") as file:
        key_events = pickle.load(file)

    controller = pynput.keyboard.Controller()
    for key, event_type in key_events:
        if event_type == KeyEventType.PRESS:
            controller.press(key)
        else:
            controller.release(key)


def main():
    """omnimacro's main entry point."""

    namespace = parse_cmd_args()
    if namespace.play:
        play_key_events(namespace.path)
    else:
        log_key_events(namespace.path)


if __name__ == "__main__":
    main()
