#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hi, \nI'm Syn-Video-Compressor \nYou can Compress Telegram Videos \n\n/help for more details."
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "š„ Downloading š„ \n"
    
    UPLOAD_START = "š¤ Uploading š¤ \n"
    
    COMPRESS_START = "š Trying to compress ... š"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "š„ Downloaded in {}\n\nš Compressed in {}\n\nš¤ Uploaded in {}"

    COMPRESS_PROGRESS = "ā³ ETA: {}\nš Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "ā Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "ā Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "ā Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "ā ļø Already One Process going on! ā ļø"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "How to Use Me? Follow These steps! \n\n1. Send me your Telegram Video. \n2. Reply the file - /compress And Persentage \nEg: <code>/compress 50</code> \n\nIf bot didn't respond, contact @synuser"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
