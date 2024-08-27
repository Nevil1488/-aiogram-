from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

router=Router()

@router.message(Command(''))
async def command(message:Message):
    await message.answer('')

@router.message(CommandStart())
async def command(message:Message):
    await message.answer('')

@router.callback_query(F.data=='')
async def callback(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer('')


class Reg(StatesGroup):
    name=State()

@router.message(Command(''))
async def reg(message:Message,state:FSMContext):
    await state.set_state(Reg.name)
    await message.answer('')

@router.message(Reg.name)
async def reg2(message:Message,state:FSMContext):
    await state.update_data(name=message.text)
    data=await state.get_data()
    await message.answer(f'Hi,{data["name"]}! ')
    await state.clear()