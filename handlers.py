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
@router.message(Command('Старт'))
async def start_one(message:Message, state: FSMContext):
    await state.set_state(Reg.parent_name)
    await message.answer('Введите своё ФИО')
@router.message(Reg.parent_name)
async def reg_two(message:Message, state: FSMContext):
    await state.update_data(parent_name=message.text)
    await state.set_state(Reg.ID)
    await message.answer('Введите идентификационный номер')
@router.message(Reg.ID)
async def reg_two(message:Message, state: FSMContext):
    await state.update_data(ID=message.text)
    await state.set_state(Reg.code)
    await message.answer('Введите код')
@router.message(Reg.code)
async def reg_two(message:Message, state: FSMContext):
    await state.update_data(code=message.text, parent_id = message.from_user.id)
    await state.update_data()
    data = await state.get_data()
    await message.answer(f'Успешно.\n {data["parent_name"]}\n {data["ID"]}\n {data["code"]}\n {data["parent_id"]}')
    parent_log_reg(data)
    await state.clear()
@router.message(Command('Send'))
async def Send(types : Message, bot):
    await asyncio.sleep(5)
    while True:
        row_count, Success = check()
        print("row count --", row_count, Success)
        print(Success)
        if Success == True:
            for i in range(row_count):
                enter, status, par_id, idlog, Time, Group, engine = rassilka(i)
                time = Time.strftime("%H:%M:%S")
                otpr, verify = check_rasp(status, Time, Group)
                if otpr == "Нет занятий":
                    Text = f"Нет занятий, время {time}"
                    await bot.send_message(chat_id=par_id, text=Text)
                if verify == False and otpr == "Опоздал":
                    Text = f"Ребенок опоздал, пришел в {time} "
                    await bot.send_message(chat_id=par_id, text=Text)
                if verify == True and otpr == "Вошел в учебное заведение":
                    Text = f"Ребенок вошел в учебное заведение, пришел в {time} "
                    await bot.send_message(chat_id=par_id, text=Text)
                if verify == True and otpr == "вышел из учебного заведения":
                    Text = f"Ребенок вышел из учебного заведения, вышел в {time}"
                    await bot.send_message(chat_id=par_id, text=Text)
                if verify == False and otpr == "вышел из учебного заведения":
                    Text = f"Ребенок вышел из учебного заведения, вышел в {time}"
                    await bot.send_message(chat_id=par_id, text=Text)
                print(par_id, row_count, idlog)
                idlog = idlog
                rewrite_id(idlog)
        elif Success == False:
            print("Обновлений нет")
        await asyncio.sleep(10)
@router.message(Command("S"))
async def S(message: types.Message,
            command : CommandObject):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    argue = command.args
    entry(argue)