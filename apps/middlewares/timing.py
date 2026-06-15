import time

from fastapi import Request

'''
    function:时间测量
'''
async def timing_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Timing"] = f"{duration}"
    return response