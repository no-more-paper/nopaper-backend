def run():
    import uvicorn
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run()
