from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
# overcome cors issue
from fastapi.middleware.cors import CORSMiddleware

# to render html
from fastapi.templating import Jinja2Templates

# initialize application
app = FastAPI()