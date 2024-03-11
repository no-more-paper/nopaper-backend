# SPDX-FileCopyrightText: 2024-present ZanSara <github@zansara.dev>
#
# SPDX-License-Identifier: AGPL-3.0-only
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer


app = FastAPI(
    title="NoPaper",
    description="NoPaper API",
    version="0.1.0",
    root_path="/api/v1",
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


from app.docs.router import router
app.include_router(router)
