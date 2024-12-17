# MammothCyber_TH


## Run the scripts:

* env build
    ```
    docker compose build
    docker compose up -d
    docker compose exec py2db python library_create.py
    docker compose exec py2db python library_add.py
    ```
* running cache demo
    ```
    docker compose exec py2db python demo_cache.py
    ```

## Explanation

Our core design is at cache.py

that there are 2 local var

