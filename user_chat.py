# from stream_chat import StreamChat
# import os
#
# # class Chat:
# #     def __init__(self):
# #         self.chat = StreamChat(api_key='7dxqchndfcjv',
# #                                api_secret='6h5c5kggc3sqjtuav56dcepttxgju9bje4e2c8bf7f3kx23fwpwhakmvvtv43x3v')
# import asyncio
# from stream_chat import StreamChatAsync
#
#
# async def main():
#     async with StreamChatAsync(api_key="xxuwa5wyd6my",
#                                api_secret="wsqw54sa52v9kakbk5qjrqqht5b6sf76enke9zhtf5ed5gts5v5g9wwap9mehqht") as chat:
#         # add a user
#
#         # create a channel about kung-fu
#         channel = chat.channel("messaging", "kung-fu")
#
#         # add a first message to the channel
#         await channel.send_message({"text": "I love you man"}, "chuck")
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(main())
#     finally:
#         loop.run_until_complete(loop.shutdown_asyncgens())
#         loop.close()
