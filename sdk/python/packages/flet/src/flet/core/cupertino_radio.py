from typing import Any, Optional, Union

from flet.core.animation import AnimationValue
from flet.core.badge import BadgeValue
from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.ref import Ref
from flet.core.tooltip import TooltipValue
from flet.core.types import (
    ColorEnums,
    ColorValue,
    LabelPosition,
    OffsetValue,
    OptionalControlEventCallable,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class CupertinoRadio(ConstrainedControl):
    """
    Radio buttons let people select a single option from two or more choices.

    -----

    Online docs: https://flet.dev/docs/controls/cupertinoradio
    """

    def __init__(
        self,
        label: Optional[str] = None,
        value: Optional[str] = None,
        label_position: Optional[LabelPosition] = None,
        fill_color: Optional[ColorValue] = None,
        active_color: Optional[ColorValue] = None,
        inactive_color: Optional[ColorValue] = None,
        autofocus: Optional[bool] = None,
        use_checkmark_style: Optional[bool] = None,
        toggleable: Optional[bool] = None,
        focus_color: Optional[ColorValue] = None,
        on_focus: OptionalControlEventCallable = None,
        on_blur: OptionalControlEventCallable = None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: Optional[AnimationValue] = None,
        animate_size: Optional[AnimationValue] = None,
        animate_position: Optional[AnimationValue] = None,
        animate_rotation: Optional[AnimationValue] = None,
        animate_scale: Optional[AnimationValue] = None,
        animate_offset: Optional[AnimationValue] = None,
        on_animation_end: OptionalControlEventCallable = None,
        tooltip: TooltipValue = None,
        badge: Optional[BadgeValue] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            badge=badge,
            visible=visible,
            disabled=disabled,
            data=data,
        )
        self.value = value
        self.label = label
        self.label_position = label_position
        self.autofocus = autofocus
        self.use_checkmark_style = use_checkmark_style
        self.fill_color = fill_color
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.on_focus = on_focus
        self.on_blur = on_blur
        self.focus_color = focus_color
        self.toggleable = toggleable

    def _get_control_name(self):
        return "cupertinoradio"

    # value
    @property
    def value(self) -> Optional[str]:
        return self._get_attr("value", def_value="")

    @value.setter
    def value(self, value: Optional[str]):
        self._set_attr("value", value)

    # label
    @property
    def label(self) -> Optional[str]:
        return self._get_attr("label")

    @label.setter
    def label(self, value: Optional[str]):
        self._set_attr("label", value)

    # label_position
    @property
    def label_position(self) -> Optional[LabelPosition]:
        return self.__label_position

    @label_position.setter
    def label_position(self, value: Optional[LabelPosition]):
        self.__label_position = value
        self._set_enum_attr("labelPosition", value, LabelPosition)

    # fill_color
    @property
    def fill_color(self) -> Optional[ColorValue]:
        return self.__fill_color

    @fill_color.setter
    def fill_color(self, value: Optional[ColorValue]):
        self.__fill_color = value
        self._set_enum_attr("fillColor", value, ColorEnums)

    # focus_color
    @property
    def focus_color(self) -> Optional[ColorValue]:
        return self.__focus_color

    @focus_color.setter
    def focus_color(self, value: Optional[ColorValue]):
        self.__focus_color = value
        self._set_enum_attr("focusColor", value, ColorEnums)

    # toggleable
    @property
    def toggleable(self) -> bool:
        return self._get_attr("toggleable", data_type="bool", def_value=False)

    @toggleable.setter
    def toggleable(self, value: Optional[bool]):
        self._set_attr("toggleable", value)

    # on_focus
    @property
    def on_focus(self) -> OptionalControlEventCallable:
        return self._get_event_handler("focus")

    @on_focus.setter
    def on_focus(self, handler: OptionalControlEventCallable):
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    def on_blur(self) -> OptionalControlEventCallable:
        return self._get_event_handler("blur")

    @on_blur.setter
    def on_blur(self, handler: OptionalControlEventCallable):
        self._add_event_handler("blur", handler)

    # autofocus
    @property
    def autofocus(self) -> bool:
        return self._get_attr("autofocus", data_type="bool", def_value=False)

    @autofocus.setter
    def autofocus(self, value: Optional[bool]):
        self._set_attr("autofocus", value)

    # use_checkmark_style
    @property
    def use_checkmark_style(self) -> bool:
        return self._get_attr("useCheckmarkStyle", data_type="bool", def_value=False)

    @use_checkmark_style.setter
    def use_checkmark_style(self, value: Optional[bool]):
        self._set_attr("useCheckmarkStyle", value)

    # active_color
    @property
    def active_color(self) -> Optional[ColorValue]:
        return self.__active_color

    @active_color.setter
    def active_color(self, value: Optional[ColorValue]):
        self.__active_color = value
        self._set_enum_attr("activeColor", value, ColorEnums)

    # inactive_color
    @property
    def inactive_color(self) -> Optional[ColorValue]:
        return self.__inactive_color

    @inactive_color.setter
    def inactive_color(self, value: Optional[ColorValue]):
        self.__inactive_color = value
        self._set_enum_attr("inactiveColor", value, ColorEnums)