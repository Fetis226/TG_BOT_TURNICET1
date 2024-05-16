from aiogram import Router
import logging
import asyncio
from BD import parent_log_reg, rassilka, entry, check, rewrite_id, check_rasp
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command, CommandObject
from aiogram.types import Message
from config_reader import config
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import datetime

router = Router()
class Reg(StatesGroup):
    parent_name = State()
    ID =State()
    code = State()
    parent_id = State()