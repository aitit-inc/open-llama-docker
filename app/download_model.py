# Run in advance to use the model offline
from huggingface_hub import snapshot_download

# download_path = snapshot_download(repo_id='openlm-research/open_llama_3b')
download_path = snapshot_download(repo_id='openlm-research/open_llama_7b')
print('Downloaed at:', download_path)
