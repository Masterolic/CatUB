# Copyright (C) 2021 KeinShin@Github.

import os
from pyrogram.methods.utilities import remove_handler

from pyrogram.types.messages_and_media import message
from system.Config import Variable as Var
from pyrogram.types import (   InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup



)

ASISTANT_CMD_ROWS = os.environ.get("ASISTANT_CMD_ROWS", None)
if ASISTANT_CMD_ROWS is None:
   number_of_rows_in_commands = 6







ASISTANT_CMD_COLUMNS = os.environ.get("ASISTANT_CMD_COLUMNS", None)
if ASISTANT_CMD_COLUMNS is None:

   number_of_columns_in_commands = 3

from system import *
from math import ceil
from pyrogram import filters

Friends = {}
from system.Config.utils import language, errors2, errors_s
from system.decorators import inline_help_wrapprs, owner

plugs = []
tgbot = bot
g = Variable.TG_BOT_USER_NAME
USER = str(Var.OWNER_NAME)

PM_MSG = os.environ.get("PM_MSG", None)
if PM_MSG is None:
    BOT_LIT = f"Hello Sir MySelf Black Lightning Here For  {USER}'s Protection "
else:
    BOT_LIT = PM_MSG   


PM_PIC = os.environ.get("PM_PIC", None)
if PM_PIC is None:
    PM_SECURITY_IMG = "https://telegra.ph/file/07d55d71944a852ac6d5e.jpg"
else:
    PM_SECURITY_IMG = PM_PIC






@bot.on_inline_query()
async def inline_handler(client, inline_query):
    fuking_sucking = await app.get_me()
    a = fuking_sucking.id
    text = inline_query.query
    if text == "Help Menu":
        content = InputTextMessageContent("**Black Lightning Help Menu for User** [{}]({})".format(USER[1:],  f"tg://user?id={fuking_sucking.id}"))
        await client.answer_inline_query(
            inline_query.id,
            results=[
                (
                    InlineQueryResultArticle(
                        title="Menu",
                        reply_markup=InlineKeyboardMarkup(help_menu(0, CMD_LIST, 'help')),
                        input_message_content=content,
                    )
                )
            ],
            cache_time=0

        )


    elif inline_query.from_user.id == a and text.lower() == "need" and "Traceback" in errors_s():
       
        await client.answer_inline_query(inline_query.id,
            cache_time=0,
            results = InlineQueryResultArticle(
        
 
              "Click for the help",
              text=f"**How If you Faced Problem \n{USER}** \nChoose Your Problem For Help ",
              reply_markup=
                InlineKeyboardMarkup(
                [InlineKeyboardButton("Commands Not Working🥺", url="https://t.me/lightning_support_grup")],
                [InlineKeyboardButton("Help Article 🤓", url="https://app.gitbook.com/@poxsisofficial/s/help/")],
                [
                    InlineKeyboardButton(
                
                    "Want To Learn CMDS😅",
                    url="https://t.me/lightning_support_grup" ,
                    )
                ], )
              )
             )
              
              

    elif inline_query.from_user.id == a and text == "**Black":
        mrkup=[

                [   InlineKeyboardButton(
                        f"{language('My Friend')}❤️❤️",
                        callback_data ="he_sucks",
                    )
                ],
                [InlineKeyboardButton(f"{language('Request')}🙏", callback_data ="fck_ask")],
                [
                    InlineKeyboardButton(
                        f"{language('Urgent')}", 
                        callback_data ="urgent",)
                        
                    ]]
  
        await client.answer_inline_query(
            inline_query.id,
            cache_time=1,
            results=InlineKeyboardMarkup(mrkup)

        
        )
    elif  text == "Assistant Menu":
        fucking_sucking = await bot.get_me()
        text = inline_query.query

        content = InputTextMessageContent("**Black Lightning ASSISTANT Help Menu for User** [{}]({})".format(USER[1:],  fucking_sucking.id))
        await inline_query.answer(result=[
        InlineQueryResultArticle(
                    
                    title="Help Menu",
                    input_message_content=content,
                    description="Help for command",
                    reply_markup=InlineKeyboardMarkup(assitant_help(0, ASSISTANT_HELP, "help")),
        )],
        cache_time=1)


blocked =[]
def blocked_user(name):
    blocked.append(name)

    


@bot.on_callback_query(filters.regex(pattern="help_next\((.+?)\)"))
@inline_help_wrapprs
async def query_hndr(client, message):
    b=await app.get_me()
    if message.from_user.id  == b.id:  # pylint:disable=E0602
        client_page = int(message.matches[0].group(1))
        reply_markup = help_menu(
            client_page + 1, CMD_LIST, "help"  # pylint:disable=E0602
        )
        await message.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(reply_markup))
    else:
      
        client_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"

        await message.answer(client_is_best, cache_time=0, show_alert=True)


            # Thanks To Friday For This Deatiled Idea of detail button
@bot.on_callback_query(filters.regex(pattern="detailed_(.*)"))

async def detailed(client, message):

    light_pulu_name = message.matches[0].group(1)
    aa = f"{light_pulu_name}'s help"
    try:
            if light_pulu_name in COMMAND_HELP:
                    lightning_help_strin = f"{language('Commands found in')} {light_pulu_name}:\n"
                    lightning_help_strin += f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{COMMAND_HELP[aa]}"
                    lightning_help_strin += "\n    " + light_pulu_name
                    lightning_help_strin += "\n"
                    o  = [
                        [InlineKeyboardButton("ᴅᴇʟᴇᴛᴇ", callback_data ="krish_{}".format(light_pulu_name)
                )],
                        [InlineKeyboardButton("нσмє 💢", callback_data ="back_(.*)")],
              ],
                    await message.edit_message_reply_markup(
                    text=lightning_help_strin,
                    reply_markup=InlineKeyboardMarkup(o)
                
        )
            else:
                await message.answer(f"{language('No Deatiled Help For Command')} {light_pulu_name}", cache_time=0, show_alert=True)
    
     
                

              
        
    except KeyError:
           await message.answer(f"{language('No Details')} U_U", cache_time=0, show_alert=False)
    
 
                
@bot.on_callback_query(filters.regex(pattern="_lightning_plugins_(.*)"))

@inline_help_wrapprs

async def query_hndr(client, message):

    light_pulu_name = message.matches[0].group(1)
    pg_no = int(message.matches[0].group(1))
    
    if light_pulu_name in COMMAND_HELP:
       
       client_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{COMMAND_HELP[light_pulu_name]}"
       client_is_best = client_help_strin 
       client_is_best += "\n\n**In Case Any Problem @lightning_support_grup** ".format(light_pulu_name)
    


    await message.edit_message_reply_markup(
         client_help_strin,
         reply_markup=InlineKeyboardMarkup([
          [InlineKeyboardButton("ᗪETᗩIᒪEᗪ", callback_data="detailed_{}".format(light_pulu_name)
          )],
          [InlineKeyboardButton("Ⴆαƈƙ 💢", callback_data="back_{}".format(pg_no))],
      ],
        )

    
@bot.on_callback_query(filters.regex(pattern="help_prev\((.+?)\)")))

@inline_help_wrapprs
async def query_hndr(client, message): 
    lightning_page = message.matches[0].group(1)
    reply_markup = help_menu(
        lightning_page - 1, CMD_LIST, "help"  # pylint:disable=E0602
    )
    await message.edit_message_reply_markup(reply_markup=reply_markup)




@bot.on_callback_query(filters.regex(pattern="lightning_is_here_cant_spam"))
@owner
async def lightning_is_better(client, message):

    user = await app.get_users(int(message.chat.id))
    text1 = f"**Byy👋**!\n**You've been blocked have fun\n\n**If you think this is a mistake contact master via {g}**"
    app.block_user(user.id)
    blocked_user(user.first_name)
    await app.send_message(message.chat_id, text1)


urgent = []




def add_friend(name, id):
    Friends.update({name: id})
def add_urgent(name):
    urgent.append(name)



@bot.on_callback_query(filters.regex(pattern="urgent"))
async def lightning_is_better(client, message):
    a = await app.get_me()
    user = await app.get_users(int(message.chat.id))

    if user.is_self :
        await message.answer("This command if for stranger not for the owner!", cache_time=0, show_alert=True)
        return

    name = user.first_name
    bhat = user.status  
    text1 = "**Hello User {},  master was last online on {}**\n**Kindly wait for him to be online :)** ".format(name, bhat)
    await app.send_message(message.chat_id, text1)
    await app.send_message(
        Variable.LOGS_CHAT_ID,
        f"**Hello {USER}, [{name}]({user.id}) wants to dicuss something important!.**",
    )
    if user.is_deleted:
     return
    add_urgent(name)






@bot.on_callback_query(filters.regex(pattern="he_sucks"))
@owner
async def lightning_is_better(client, message):
    user =   await app.get_users(int(message.chat.id))
    o = await app.get_me()
    owner = await app.get_users(int(o.id

    ))
    user_id = user.id
    await message.edit(f"**Hello {user.first_name} if u are friend kindly contact him via {g}**\n\n__{USER}:- was last online on__ {owner.last_online_date}")

    
    
    
    
    
    




@bot.on_callback_query(filters.regex(pattern="fck_ask"))
@owner
async def lightning_is_better(client, message):
    user =   await app.get_users(int(message.chat.id))
    bot_id = await bot.get_me()
    bot_id = bot_id.id
    await message.edit
    btn =InlineKeyboardMarkup([InlineKeyboardButton("Contact Him", url=f"tg://user?id={bot_id}")])

    await app.send_message(
        user.id,
        f"Master is busy for some reason contact him via bot link given below",
        reply_markup=btn,
    )


          




@bot.on_callback_query(filters.regex(pattern="krish_(.*)"))
@inline_help_wrapprs
async def chill(client, message):

    file=message.matches[0].group(1)
    pg_no=int(message.matches[0].group(1))
    await message.edit(
            f"`File and plugin Removed`",
            reply_markup=InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Ⴆαƈƙ 💢", data="back_{}".format(pg_no))],

        ],)
    )
    os.remove('system/plugins/' + file + ".py" )
    logging.info("REMOVED:- {}".format(file))
    
# Thanks To Friday Userbot and @Midhun_xD For This idea







@bot.on_callback_query(filters.regex(pattern="back_(.*)"))
@inline_help_wrapprs
async def ho(client, message):
    o=message.matches[0].group(1)
    await message.answer("Returned To Home", cache_time=0, show_alert=False)
    reply_markup = help_menu(o, CMD_LIST, "help")
    ho = f"""**Black Lightning {language('help menu')}**: {language('Commands')}: {len(CMD_LIST)}"""
    await message.edit(ho, reply_markup=InlineKeyboardMarkup(reply_markup))





        


def help_menu(pg_num, setv, prefix):
    rows = 7
    columns = 3
    helpable_modules = []
    for p in setv:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [
        InlineKeyboardButton(
            text="{} {} {}".format("⨵", x, "⨵"),
            callback_data="_lightning_plugins_{}".format(x, pg_num),
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::columns], modules[1::columns]))
    if len(modules) % columns == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / rows)
    page = pg_num % max_num_pages
    if len(pairs) > rows:
        pairs = pairs[
            page * rows : rows * (page + 1)
        ] + [
            (
                InlineKeyboardButton(
                    text="Previous",
                    callback_data="{}_prev({})".format(prefix, pg_num),),
                InlineKeyboardButton(
                    text="Next",
                    callback_data="{}_next({})".format(prefix, setv),
                ),
            )
        ]
    return pairs


@bot.on_message(filters.command(["Commands"]) & filters.incoming)
async def command(client ,event):
    for i in ASSISTANT_HELP:
        if i.startswith('_'):
            return
        plugs.append(i)
    des = sorted(plugs)
    
    buttons = assitant_help(0, ASSISTANT_HELP, 'help')
    if des in ASSISTANT_HELP:

     await event.edit_message_reply_markup(reply_markup =buttons)

@bot.on_callback_query(filters.regex(pattern="_cmd_data_(.*)"))

async def lightning_pugins_query_hndlr(client ,event):
    command = ASSISTANT_HELP['Command']
    cmd = event.matches[0].group(1)
    type = ASSISTANT_HELP[f"{cmd}'s Type"]
    try:
    
     if cmd in ASSISTANT_HELP:
        assistant_help_strin = f"**✡ Type : {type} ✡**"
        assistant_help_strin  += f"**🔺 COMMAND 🔺 :** `{cmd}` \n\n{command}"
        
        assistant_buttons = assistant_help_strin 
        assistant_buttons += "\n\n**In Case Any Problem @lightning_support_grup**".format(cmd)
        await event.edit(assistant_buttons)
    
    except KeyError:
        await event.answer("The command isn't displayable", cache_time=0, alert=True)


@bot.on_callback_query(filters.regex(pattern="help_preve\((.+?)\)"))

async def lightning_pugins_query_hndlr(client, lightning):
    
        lightning_page = int(lightning.matches[0].group(1))
        buttons = assitant_help(
            lightning_page - 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        await lightning.edit_message_reply_markup(reply_markup=buttons)

import io
# from system.sqls.bot_sql import *

# @bot.on_callback_query(filters.regex(pattern="users"))


# async def d(client ,message):
#     with io.BytesIO(str.encode(get_ids())) as out_file:
#         out_file.name = "cmd_list.txt"
#     await bot.send_document(message.chat.id, document=out_file)

@bot.on_callback_query(filters.regex(pattern="help_nexte\((.+?)\)"))
  
async def ass_pugins_query_hndlr(client, lightning):
        await lightning.delete()
        lightning_page = int(lightning.matches[0].group(1))
        
        buttons = assitant_help(
            lightning_page + 1, ASSISTANT_HELP, "help"  # pylint:disable=E0602
        )
        await lightning.edit_message_reply_markup(reply_markup=buttons)



#    Copyright (C) 2020 Telebot

def assitant_help(b_lac_krish, lists, lightning_lol):

 total_cmds = []
 for p in list:
     if not p.startswith("_"):
         total_cmds.append(p)
 total_cmds = sorted(total_cmds)
 plugins = [
     InlineKeyboardButton(
         "{}".format( x), callback_data="_cmd_data_{}".format(x)
     )
     for x in total_cmds
 ]
 pairs = list(zip(plugins[::number_of_columns_in_commands], plugins[1::number_of_columns_in_commands]))
 if len(plugins) % number_of_columns_in_commands == 1:
     pairs.append((plugins[-1],))
 max_fix = ceil(len(pairs) / number_of_rows_in_commands)
 total_cmds_pages = b_lac_krish % max_fix
 
 if len(pairs) > number_of_rows_in_commands:
   

     pairs = pairs[
         total_cmds_pages * number_of_rows_in_commands : number_of_rows_in_commands * (total_cmds_pages + 1)
     ] + [
         (
             InlineKeyboardButton(
                 "Previous", callback_data="{}_prev({})".format(lightning_lol, total_cmds_pages)
             ),
            
            InlineKeyboardButton(
                 "Next", callback_data="{}_next({})".format(lightning_lol, total_cmds_pages)
             ),
             
         )
     ]
 else:
   pairs = pairs[
       total_cmds_pages * number_of_rows_in_commands : number_of_columns_in_commands * (total_cmds_pages + 1)
   
   ]

 return pairs

