const { Telegraf } = require('telegraf')
const { message } = require('telegraf/filters');
const { link, FmtString } = require("telegraf/format");
require('dotenv').config()

const HEADER_IMAGE_URL = "./public/welcome-message-header.jpg"

const POST_TEXT = `
🤝Благодарю за подписку!

В качестве подарка составил для тебя список самых полезных каналов для саморазвития.
   
🧠<a href="https://t.me/+-FOEdpd-h-I1ZWYy">OLYMPIA</a> - все тонкости мужской психологии, раскрытие женских приемов манипуляции.

👁<a href="https://t.me/+WznZg97FDP80NjRi">Границы мужества</a> - канал, вдохновляющий на преодоление жизненных вызовов и расширение границ собственных возможностей.
`;


const bot = new Telegraf(process.env.BOT_TOKEN)
bot.start((ctx) => {
    ctx.sendPhoto({
        source: HEADER_IMAGE_URL,
    }, {
        caption: POST_TEXT,
        parse_mode: "HTML"
    })

})
bot.help((ctx) => ctx.reply('Send me a sticker'))
bot.on(message('sticker'), (ctx) => ctx.reply('👍'))
bot.hears('hi', (ctx) => ctx.reply('Hey there'))
bot.launch()

// Enable graceful stop
process.once('SIGINT', () => bot.stop('SIGINT'))
process.once('SIGTERM', () => bot.stop('SIGTERM'))
