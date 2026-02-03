#!/usr/bin/env python3
"""Telegram bot with menu commands and a photo welcome message."""
import os

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes


OWNER_MENU_TEXT = (
    "𖤊───⪩ OWNER MENU ⪨───𖤊\n\n"
    "✦ /addprem <id>\n"
    "  ↳ Grant premium access to a user.\n\n"
    "✦ /delprem <id>\n"
    "  ↳ Revoke premium access from a user.\n\n"
    "✦ /addowner <id>\n"
    "  ↳ Add a new owner with full system control.\n\n"
    "✦ /delowner <id>\n"
    "  ↳ Remove an existing owner.\n\n"
    "✦ /listprem\n"
    "  ↳ Show all premium users.\n\n"
    "✦ /listvip\n"
    "  ↳ Show all VIP users.\n\n"
    "✦ /delvip <id>\n"
    "  ↳ Remove a VIP user.\n\n"
    "✦ /cekidgrup\n"
    "  ↳ Check the current group’s unique ID.\n\n"
    "✦ /listidgrup\n"
    "  ↳ Display all stored group IDs.\n\n"
    "✦ /listsender\n"
    "  ↳ Display all sender bots.\n\n"
    "✦ /delsender <id>\n"
    "  ↳ Delete sender bot.\n\n"
    "✦ /listdevice\n"
    "  ↳ Display all device numbers."
)

BUG_MENU_TEXT = (
    "𖤊───⪩ BUG MENU ⪨───𖤊\n\n"
    "For safety and compliance, this bot does not provide disruptive or abusive actions.\n"
    "Use this menu for diagnostics and support instead:\n\n"
    "✦ /status\n"
    "  ↳ Show bot status and uptime.\n\n"
    "✦ /report <message>\n"
    "  ↳ Send a support report to the admins.\n\n"
    "✦ /limits\n"
    "  ↳ Display usage limits and premium tiers.\n\n"
    "Purchased access provides limited features and priority support.\n"
    "— Produced by AlannXD Labs."
)


def build_welcome_caption() -> str:
    logo_text = (
        "<b>ALANNXD LABS</b>\n"
        "<code>BOT • COMMAND CENTER</code>\n"
        "<i>Uppercase styling with glow-inspired emphasis.</i>"
    )
    menu_hint = "\n\nUse /owner_menu or /bug_menu to view command lists."
    return f"{logo_text}{menu_hint}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    caption = build_welcome_caption()
    photo_url = os.getenv("BOT_WELCOME_PHOTO_URL")
    photo_path = os.getenv("BOT_WELCOME_PHOTO_PATH")

    if photo_url:
        await update.message.reply_photo(photo=photo_url, caption=caption, parse_mode=ParseMode.HTML)
        return

    if photo_path and os.path.exists(photo_path):
        with open(photo_path, "rb") as photo_file:
            await update.message.reply_photo(photo=photo_file, caption=caption, parse_mode=ParseMode.HTML)
        return

    await update.message.reply_text(caption, parse_mode=ParseMode.HTML)


async def owner_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(OWNER_MENU_TEXT)


async def bug_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(BUG_MENU_TEXT)


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Missing TELEGRAM_BOT_TOKEN environment variable.")

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("owner_menu", owner_menu))
    application.add_handler(CommandHandler("bug_menu", bug_menu))

    application.run_polling()


if __name__ == "__main__":
    main()
