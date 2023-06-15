# Docker env of open-llama

# Requirements
- Docker

# Build
```shell
bin/dev build
```

# Run
```
bin/dev run app /bin/bash

# In the container
python /app/main.py
```

# Download model in advance and load from local path
Edit `app/download_model.py` and run to download.
```shell
# Run in host
# Need huggingface-hub package.
python app/download_model.py
```

Move the model directory into `./models/` like following.
```
./models/models--openlm-research--open_llama_3b
```

Edit `app/main.py` to load this model.

You need to specify not the above path but the hash value directory under the snapshot dir like this.
```
/models/models--openlm-research--open_llama_3b/snapshots/8fcddba529aef0eda7293cc9a4171a3994648d2e
```