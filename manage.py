from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import requests
import re


def get_url(url):
    scihub_url = 'https://sci-hub.do/'+url
    print("@@@@@@@@@@@",scihub_url)
    contents = requests.get(scihub_url)
    txt = contents.text
    p = "'(.)*sci-hub\.(.)*\.pdf\?(.)*'"
    start = re.search(p, txt)
    try:
        url = start[0][1:-1]
        if(url[0:2] =="//"):
            url = url[2:]
        return url
    except:
        return "false"


def article(bot, update):
    print("bot",bot)
    print("update",update)
    text = update.message.text
    if(text == "/about"):
        url_result="noting"
        url_result = str(url_result)
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id,text=url_result)

    elif(text == "/donate"):
        url_result ="\n💲 The project is supported by user donations 💲\n\n{BTC}\n\n{LTC}\n\n{XMR}\n\n{Verge}".format(BTC=" BTC: 34YBJZnKzNsx8xA6dCMGWB8K9VMSV3DG86 💰",LTC=" LTC: LZBCxXNf2dBLeCEs4b2d14GNU5RrpoXc5P 💰",XMR="XMR: 82aB7Hdc1Ek21gULnksNEiPtw7XaFNPhShj3afV5czyTjNMRJbBYARYTtXXQ1xHQNBZZN3R5YLMkJEdSYyNEqGaw6V4Mdkd 💰",Verge="XVG: DNYQfU6soMJ58SSz4ub7BgQpzYr29qjWYh 💰")
        url_result = str(url_result)
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id,text=url_result)
    elif(text == "/help" or text =="/start"):
        url_result ="enter the article url or doi for  ex:https://ieeexplore.ieee.test/document/8876896 doi:10.1109/Deep-ML.2019.00011"
        url_result = str(url_result)
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id,text=url_result)

    else:
        url_result = get_url(str(text))
        if(url_result != "false"):
            chat_id = update.message.chat_id
            bot.send_document(chat_id=chat_id, document=url_result)
        else:
            chat_id = update.message.chat_id
            bot.send_message(chat_id=chat_id,text="not found article")
    print("================",url_result)
#    url_result = url_result
    chat_id = update.message.chat_id
    #print("====",chat_id)


def main():
    updater = Updater('1092156256:AAG5VSCrui6MjxNN6_WSIr3YqZqpDcwqzFk')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text,article))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



