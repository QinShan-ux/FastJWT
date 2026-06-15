from collections import defaultdict

from fastapi import Request
from starlette.responses import JSONResponse
'''
    function: ip限制
'''
request_counts = defaultdict(int)
blank = []
async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host

    if ip in blank:
        return JSONResponse(status_code=403,
                            content={"message": "禁止访问"})

    # 简单限流（生产用 Redis）
    request_counts[ip] += 1
    if request_counts[ip] >= 100:
        return JSONResponse(status_code=403,
                            content={"message": "请求过于频繁"})

    return await call_next(request)