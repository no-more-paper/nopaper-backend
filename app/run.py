# SPDX-FileCopyrightText: 2024-present ZanSara <github@zansara.dev>
#
# SPDX-License-Identifier: AGPL-3.0-only
def run():
    import uvicorn
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()
