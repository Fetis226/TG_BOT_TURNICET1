from aiogram import Router
import asyncio
from BD import parent_log_reg, rassilka, entry, check, rewrite_id, check_rasp
from aiogram import types
from encoder import export_log
from aiogram.filters.command import Command, CommandObject
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

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
        if Success == True:
            for i in range(row_count):
                enter, status, par_id, idlog, Time, Group, engine = rassilka(i)
                time = Time.strftime("%H:%M:%S")
                otpr = check_rasp(status, Time, Group)
                Text = f'{otpr}, {time}'
                await bot.send_message(chat_id=par_id, text=Text)
                export_log()
                idlog = idlog
                rewrite_id(idlog)
        elif Success == False:
            print("Обновлений нет")
        await asyncio.sleep(120)
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