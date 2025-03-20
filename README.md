# Taskify - Frontend

Live Link: https://shera-nextjs-app.vercel.app/

```
Tech: NextJS | Flask + Flask-Restful
DB  : Supabase (Postgres) Cloud
ORM : SQLAlchemy

Back-End Architecture: Application Factory Pattern + Blueprint (Scalable)

Deployed In-
Front-End: Vercel
Back-End : Render
```

## FEATURES

-   Add Task
-   Empty Text Validation
-   Shows Funny Message When No Text Is Entered
-   Only Basic Symbols Allowed E.g. `!@#$%^&*()_+\-=[\]{};:'",.? `
-   Back-End Validation: Args, String Length, Emptry String Etc.
-   Filter by All, Pending, Done
-   Delete Task
-   Mark/ UnMark A Task

## NOTE

-   I Followed "Context Provider Pattern" In Front-End (NextJS) App To Minimize Re-Renders.
-   I Followed "Application Factory Pattern + Blueprint" Pattern In Back-End (Flask + Flask-Restful) So That It Can Be Scaled.
-   I Used Flask-Restful For Quickly Building Rest APIs Following OOP Pattern.
-   Completed All Given Requierments

## HOW TO RUN FRONT-END LOCALLY?

-   Clone The Repository First
-   Make Sure You Have Node Installed
-   Go To Root Folder, And Enter `npm ci` (`npm i` will work too)
-   Make Sure To Put `.env` File
-   Replace Host If Needed In `.env` File
-   Run By `npm run dev`

```
NEXT_PUBLIC_HOST = 'http://127.0.0.1:5000/api'
# NEXT_PUBLIC_HOST = 'https://shera-flask-server.onrender.com/api'
```

## HOW TO RUN BACK-END LOCALLY?

-   Clone The Repository First
-   Create Anaconda Environment With `conda create --name flask-app python`
-   Activate Environment With `conda activate flask-app`
-   Point Your Terminal To Root Of The Project
-   Install Dependencies With `pip install -r requirements.txt`
-   Make Sure To Put `.env` File
-   Replace Host If Needed In `.env` File

```
CLIENT_URI = '*'
DATABASE_URI = 'postgresql://postgres.priixfefmlsfneulxpna:yJ0aygmzdpNWiOy5@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
```

-   Run By `python server.py`
