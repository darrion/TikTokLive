# Generated by the TikTokLive compiler.
# DO NOT EDIT!
# SERIOUSLY!
# I MEAN IT!

from TikTokLive.proto.tiktok_proto import *
from TikTokLive.proto.custom_proto import *
from .base_event import BaseEvent
from typing import Type, Union, Dict
from typing import Union



class BarrageEvent(BaseEvent, WebcastBarrageMessage):
    """
    BarrageEvent
    """


class CaptionEvent(BaseEvent, WebcastCaptionMessage):
    """
    CaptionEvent
    """


class CommentEvent(BaseEvent, WebcastChatMessage):
    """
    CommentEvent
    """

    at_user: ExtendedUser
    user: ExtendedUser

    @property
    def comment(self) -> str:
        """
        The user comment content

        :return: Comment string

        """

        return self.content


class ControlEvent(BaseEvent, WebcastControlMessage):
    """
    ControlEvent
    """


class EmoteChatEvent(BaseEvent, WebcastEmoteChatMessage):
    """
    EmoteChatEvent
    """

    user: ExtendedUser


class EnvelopeEvent(BaseEvent, WebcastEnvelopeMessage):
    """
    EnvelopeEvent
    """


class GiftEvent(BaseEvent, WebcastGiftMessage):
    """
    GiftEvent
    """

    to_user: ExtendedUser
    user: ExtendedUser
    gift: ExtendedGiftStruct

    @property
    def streaking(self) -> bool:
        """
        Read the repeat_end to tell a user whether the gift is part of an ongoing streak

        :return: Whether the user is currently engaged in a streak

        """

        if not self.streakable:
            return False

        return not bool(self.repeat_end)


class GoalUpdateEvent(BaseEvent, WebcastGoalUpdateMessage):
    """
    GoalUpdateEvent
    """


class HourlyRankEvent(BaseEvent, WebcastHourlyRankMessage):
    """
    HourlyRankEvent
    """


class ImDeleteEvent(BaseEvent, WebcastImDeleteMessage):
    """
    ImDeleteEvent
    """


class LikeEvent(BaseEvent, WebcastLikeMessage):
    """
    LikeEvent
    """

    user: ExtendedUser


class LinkEvent(BaseEvent, WebcastLinkMessage):
    """
    LinkEvent
    """


class LinkLayerEvent(BaseEvent, WebcastLinkLayerMessage):
    """
    LinkLayerEvent
    """


class LinkMicArmiesEvent(BaseEvent, WebcastLinkMicArmies):
    """
    LinkMicArmiesEvent
    """


class LinkMicBattleEvent(BaseEvent, WebcastLinkMicBattle):
    """
    LinkMicBattleEvent
    """


class LinkMicFanTicketMethodEvent(BaseEvent, WebcastLinkMicFanTicketMethod):
    """
    LinkMicFanTicketMethodEvent
    """


class LinkMicMethodEvent(BaseEvent, WebcastLinkMicMethod):
    """
    LinkMicMethodEvent
    """


class LiveIntroEvent(BaseEvent, WebcastLiveIntroMessage):
    """
    LiveIntroEvent
    """

    host: ExtendedUser


class MemberEvent(BaseEvent, WebcastMemberMessage):
    """
    MemberEvent
    """

    operator: ExtendedUser
    user: ExtendedUser


class MessageDetectEvent(BaseEvent, WebcastMsgDetectMessage):
    """
    MessageDetectEvent
    """


class OecLiveShoppingEvent(BaseEvent, WebcastOecLiveShoppingMessage):
    """
    OecLiveShoppingEvent
    """


class PollEvent(BaseEvent, WebcastPollMessage):
    """
    PollEvent
    """


class QuestionNewEvent(BaseEvent, WebcastQuestionNewMessage):
    """
    QuestionNewEvent
    """


class RankTextEvent(BaseEvent, WebcastRankTextMessage):
    """
    RankTextEvent
    """


class RankUpdateEvent(BaseEvent, WebcastRankUpdateMessage):
    """
    RankUpdateEvent
    """


class RoomEvent(BaseEvent, WebcastRoomMessage):
    """
    RoomEvent
    """


class RoomPinEvent(BaseEvent, WebcastRoomPinMessage):
    """
    RoomPinEvent
    """


class RoomUserSeqEvent(BaseEvent, WebcastRoomUserSeqMessage):
    """
    RoomUserSeqEvent
    """


class SocialEvent(BaseEvent, WebcastSocialMessage):
    """
    SocialEvent
    """

    user: ExtendedUser


class SubNotifyEvent(BaseEvent, WebcastSubNotifyMessage):
    """
    SubNotifyEvent
    """

    user: ExtendedUser


class SystemEvent(BaseEvent, WebcastSystemMessage):
    """
    SystemEvent
    """


class UnauthorizedMemberEvent(BaseEvent, WebcastUnauthorizedMemberMessage):
    """
    UnauthorizedMemberEvent
    """


EVENT_MAPPINGS: Dict[str, BaseEvent] = {
    "WebcastGiftMessage": GiftEvent,
    "WebcastRoomMessage": RoomEvent,
    "WebcastBarrageMessage": BarrageEvent,
    "WebcastCaptionMessage": CaptionEvent,
    "WebcastChatMessage": CommentEvent,
    "WebcastControlMessage": ControlEvent,
    "WebcastEmoteChatMessage": EmoteChatEvent,
    "WebcastEnvelopeMessage": EnvelopeEvent,
    "WebcastGoalUpdateMessage": GoalUpdateEvent,
    "WebcastImDeleteMessage": ImDeleteEvent,
    "WebcastLikeMessage": LikeEvent,
    "WebcastRoomUserSeqMessage": RoomUserSeqEvent,
    "WebcastSocialMessage": SocialEvent,
    "WebcastSubNotifyMessage": SubNotifyEvent,
    "WebcastRankUpdateMessage": RankUpdateEvent,
    "WebcastMemberMessage": MemberEvent,
    "WebcastPollMessage": PollEvent,
    "WebcastQuestionNewMessage": QuestionNewEvent,
    "WebcastRankTextMessage": RankTextEvent,
    "WebcastHourlyRankMessage": HourlyRankEvent,
    "WebcastLinkMicArmies": LinkMicArmiesEvent,
    "WebcastLinkMicBattle": LinkMicBattleEvent,
    "WebcastLinkMicFanTicketMethod": LinkMicFanTicketMethodEvent,
    "WebcastLinkMicMethod": LinkMicMethodEvent,
    "WebcastLiveIntroMessage": LiveIntroEvent,
    "WebcastUnauthorizedMemberMessage": UnauthorizedMemberEvent,
    "WebcastMsgDetectMessage": MessageDetectEvent,
    "WebcastOecLiveShoppingMessage": OecLiveShoppingEvent,
    "WebcastRoomPinMessage": RoomPinEvent,
    "WebcastSystemMessage": SystemEvent,
    "WebcastLinkMessage": LinkEvent,
    "WebcastLinkLayerMessage": LinkLayerEvent,
}

ProtoEvent: Type = Union[
    GiftEvent,
    RoomEvent,
    BarrageEvent,
    CaptionEvent,
    CommentEvent,
    ControlEvent,
    EmoteChatEvent,
    EnvelopeEvent,
    GoalUpdateEvent,
    ImDeleteEvent,
    LikeEvent,
    RoomUserSeqEvent,
    SocialEvent,
    SubNotifyEvent,
    RankUpdateEvent,
    MemberEvent,
    PollEvent,
    QuestionNewEvent,
    RankTextEvent,
    HourlyRankEvent,
    LinkMicArmiesEvent,
    LinkMicBattleEvent,
    LinkMicFanTicketMethodEvent,
    LinkMicMethodEvent,
    LiveIntroEvent,
    UnauthorizedMemberEvent,
    MessageDetectEvent,
    OecLiveShoppingEvent,
    RoomPinEvent,
    SystemEvent,
    LinkEvent,
    LinkLayerEvent,
]

__all__ = [
    "GiftEvent",
    "RoomEvent",
    "BarrageEvent",
    "CaptionEvent",
    "CommentEvent",
    "ControlEvent",
    "EmoteChatEvent",
    "EnvelopeEvent",
    "GoalUpdateEvent",
    "ImDeleteEvent",
    "LikeEvent",
    "RoomUserSeqEvent",
    "SocialEvent",
    "SubNotifyEvent",
    "RankUpdateEvent",
    "MemberEvent",
    "PollEvent",
    "QuestionNewEvent",
    "RankTextEvent",
    "HourlyRankEvent",
    "LinkMicArmiesEvent",
    "LinkMicBattleEvent",
    "LinkMicFanTicketMethodEvent",
    "LinkMicMethodEvent",
    "LiveIntroEvent",
    "UnauthorizedMemberEvent",
    "MessageDetectEvent",
    "OecLiveShoppingEvent",
    "RoomPinEvent",
    "SystemEvent",
    "LinkEvent",
    "LinkLayerEvent",
    "ProtoEvent",
    "EVENT_MAPPINGS"
]