from fastapi import Request
from fastapi.responses import JSONResponse
from utils.crypto import aes_decrypt, aes_encrypt

async def crypto_middleware(request: Request, call_next):
    # 解密请求体
    if request.headers.get("X-Encrypted") == "true":
        try:
            raw = await request.body()
            decrypted = aes_decrypt(raw.decode())
            # 重写请求体
            async def new_body():
                yield decrypted.encode()
            request._body = decrypted.encode()
            request.state.encrypted = True
        except Exception:
            return JSONResponse(status_code=400, content={"message": "解密失败"})

    response = await call_next(request)

    # 加密响应体
    if getattr(request.state, "encrypted", False):
        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        encrypted = aes_encrypt(body.decode())
        return JSONResponse(content={"data": encrypted})

    return response