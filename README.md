# Modeling A Novel
  
<div style="text-align:center"><img src="img/book.gif" width="100%" height="225"/></div>

---

Welcome to the project named the Noveller, aka "Modeling a Novel." This project is created to help writers suffering from writers' block by generating prompting paragraphs base on their subject of choice. It is build using OpenAI GPT-2 neural network.  

<details>

<summary>What is: Generative Pre-trained Transformer (GPT)</summary>
<br>
The GPT architecture implements a deep neural network, specifically a transformer model, which uses attention in place of the previous recurrence-based and convolution-based architectures. Attention mechanisms allow the model to selectively focus on segments of input text it predicts to be the most relevant. This model provides for significantly increased parallelization and outperforms previous benchmarks for RNN/CNN/LSTM-based models.  

<br>
<br>

<details>  

<summary>Models Training Parameters</summary>

- dataset: 1105 Novels  
- model_name: 124M (retrained)  
- encoding: utf-8
- batch_size: 1  
- learning_rate: 0.00002  
- accumulate_gradients: 1  
- optimizer: adam  
- top_k: 40  

</details>

</details>

---

## References

[Royal Road](https://www.royalroad.com/home)  
[OpenAI GPT-2](https://github.com/openai/gpt-2)  
[Nshepperd GPT-2](https://github.com/nshepperd/gpt-2)  
[OpenAI GPT-2 Training Tutorial](https://www.youtube.com/watch?v=oEpLMb5D_G0&t=76s)  
