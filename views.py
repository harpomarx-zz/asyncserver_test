# -*- coding: utf-8 -*-
""" Files containing views for asyncserver project. """

from aiohttp import web
import aiohttp_jinja2

async def handle(request):
    """

    :param request:
    :return:
    """
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(body=text.encode('utf-8'))

async def wshandler(request):
    """

    :param request:
    :return:
    """
    ws = web.WebSocketResponse()

    await ws.prepare(request)

    async for msg in ws:
        if msg.tp == web.MsgType.text:
            ws.send_str("Hello, {}".format(msg.data))
        elif msg.tp == web.MsgType.binary:
            ws.send_bytes(msg.data)
        elif msg.tp == web.MsgType.close:
            break

    return ws


async def template_handler(request):
    """

    :param request:
    :return:
    """

    print(type(request))
    response = aiohttp_jinja2.render_template('base_template.html', request, {})
    print(response)
    response.headers['Content-Language'] = 'en'
    return response
