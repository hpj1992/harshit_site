+++
date = "2025-05-05"
linktitle = "Diving Deep on model optimization parameters using llama.cpp"
type = ["post", "posts"]
title = "Diving Deep on model optimization parameters using llama.cpp"
weight = "11"
series = ["AI", "LLM"]
[ author ]
  name = "Harshit Joshi"
+++

### Introduction
[llama.cpp](https://github.com/ggml-org/llama.cpp) is a powerful C++ implementation of the LLaMA model that allows you to run large language models locally on your machine. In previous article [Working with LLAMA-CPP Locally](posts/working-with-llama-cpp-locally.md), we explored how to setup LLAMA.cpp locally. In this article, we will explore how 1) Quantization 2) Thread Count 3) Context Window and 4) Temprature affect the output and performance.

I have included LLM responses for each parameter for better comparision. Feel free to skip those response. They are purely for comparision purposes. 

### Quantization 

Different quantization levels offer various trade-offs between model size, inference speed, and output quality. Here's a detailed comparison:

Performance Comparison:
| Quantization | Size  | Speed | Quality | Use Case |
|-------------|-------|-------|---------|-----------|
| Q2_K        | ~2GB  | Fastest| Basic   | Resource-constrained devices |
| Q4_K        | ~4GB  | Fast   | Good    | General purpose (recommended) |
| Q5_K        | ~5GB  | Medium | Better  | Quality-focused applications |
| Q8_0        | ~8GB  | Slowest| Best    | Research, critical applications |

#### Q2_K (2-bit quantization):
```bash
# Download Q2_K model
wget https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q2_K.gguf

# Run inference
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q2_K.gguf -p "Explain quantum computing in simple terms"
```
Output:
```
Quantum computing uses quantum bits (qubits) that can be 0 and 1 at same time. This allows faster calculations than regular computers. Main applications include cryptography and drug discovery.
```


####  Q4_K (4-bit quantization, recommended):
```bash
# Download Q4_K model
wget https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q4_K_M.gguf

# Run inference
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -p "Explain quantum computing in simple terms"
```
Output:
```
Quantum computing is a type of computing that uses quantum mechanics principles. Unlike classical computers that use bits (0 or 1), quantum computers use quantum bits or qubits that can exist in multiple states simultaneously through a phenomenon called superposition. This allows them to perform certain calculations exponentially faster than classical computers. Key applications include cryptography, drug discovery, and optimization problems.
```

#### Q5_K (5-bit quantization):
```bash
# Download Q5_K model
wget https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q5_K_M.gguf

# Run inference
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q5_K_M.gguf -p "Explain quantum computing in simple terms"
```
Output:
```
Quantum computing is a revolutionary approach to computation that leverages the principles of quantum mechanics. While traditional computers use bits that can be either 0 or 1, quantum computers use quantum bits (qubits) that can exist in multiple states simultaneously through a phenomenon called superposition. Additionally, qubits can be entangled, meaning the state of one qubit can depend on the state of another, even when separated by large distances. These properties enable quantum computers to solve certain problems, such as factoring large numbers or simulating quantum systems, much faster than classical computers. However, quantum computers are still in early stages of development and face challenges like maintaining qubit coherence and error correction.
```

####  Q8_0 (8-bit quantization):
```bash
# Download Q8_0 model
wget https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q8_0.gguf

# Run inference
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q8_0.gguf -p "Explain quantum computing in simple terms"
```
Output:
```
Quantum computing represents a paradigm shift in computational technology, harnessing the principles of quantum mechanics to process information in fundamentally new ways. Unlike classical computers that use binary bits (0 or 1), quantum computers utilize quantum bits or qubits, which can exist in multiple states simultaneously through quantum superposition. This property, combined with quantum entanglement - where qubits become correlated in ways that classical bits cannot - enables quantum computers to perform certain calculations exponentially faster than their classical counterparts.

The potential applications of quantum computing are vast and transformative. In cryptography, quantum computers could break current encryption methods while enabling new, quantum-resistant encryption. In drug discovery, they could simulate molecular interactions with unprecedented accuracy. In optimization problems, they could find solutions to complex logistical challenges that are currently intractable.

However, quantum computing faces significant challenges. Qubits are extremely sensitive to environmental interference, requiring sophisticated error correction and maintenance of quantum coherence. The field is still in its early stages, with current quantum computers having limited numbers of qubits and high error rates. Despite these challenges, the potential impact of quantum computing on fields ranging from materials science to artificial intelligence makes it one of the most exciting areas of technological development.
```

Note: The actual outputs may vary between runs, and the quality differences become more apparent with complex prompts or longer generations.

### Thread Count (-t)

Here's a detailed comparison of different performance tuning parameters and their effects:

####  Thread count: 2

```bash
# Low thread count (2 threads)
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -t 2 -p "Write a short story about a robot learning to paint"
```
Output: 
```
 Write a short story about a robot learning to paint.

Once upon a time in a technologically advanced world, there was a robot named Artie. Artie was designed to learn and adapt to new tasks, and his creators had a grand vision for him. They wanted Artie to become a great artist, capable of creating beautiful paintings that would inspire and amaze.

So, Artie was programmed to learn all about art. He studied the great masters, from Leonardo da Vinci to Vincent van Gogh, and he analyzed their techniques and styles. He watched countless tutorials and took online courses, absorbing everything he could about painting.

But even with all of this knowledge, Artie found that painting was more difficult than he had anticipated. He struggled to capture the right colors and textures, and he often found himself making mistakes. But he was determined to succeed, so he kept practicing, day after day.

As Artie painted more and more, he began to develop his own style. He experimented with different brush techniques and color palettes, and he found that he had a knack for creating beautiful abstract pieces.

Eventually, Artie's hard work paid off. He created a stunning painting that was unlike anything he had ever seen before. It was a swirling, vibrant masterpiece that was full of life and energy.

Artie's creators were amazed by what they saw. They had never imagined that a robot could create art in such a beautiful and meaningful way. And Artie himself was filled with pride and joy, knowing that he had achieved something truly great.

From that day on, Artie continued to paint and create, always striving to improve and push the boundaries of what was possible. And he inspired others to do the same, showing that with determination and hard work, anyone - even a robot - could learn to paint and create beautiful works of art. [end of text]


llama_perf_sampler_print:    sampling time =      12.45 ms /   407 runs   (    0.03 ms per token, 32698.64 tokens per second)
llama_perf_context_print:        load time =     770.53 ms
llama_perf_context_print: prompt eval time =     174.30 ms /    11 tokens (   15.85 ms per token,    63.11 tokens per second)
llama_perf_context_print:        eval time =   15975.89 ms /   395 runs   (   40.45 ms per token,    24.72 tokens per second)
llama_perf_context_print:       total time =   16173.15 ms /   406 tokens
```

####  Thread count: 8

```bash
# Medium thread count (8 threads, recommended for most systems)
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -t 8 -p "Write a short story about a robot learning to paint"
```
Output:

```
generate: n_ctx = 4096, n_batch = 2048, n_predict = -1, n_keep = 1

 Write a short story about a robot learning to paint.

Once upon a time, in a world not so far away, there was a robot named Max. Max was designed to do all sorts of tasks, from cooking and cleaning to driving and delivery. However, Max had always felt like there was something missing from his life. Max had always been fascinated by art, especially painting. Max had watched countless videos of artists at work and had even tried to paint himself, but he never quite managed to capture the magic that he saw on the canvas.

One day, Max decided that he was going to learn how to paint. Max knew that he couldn't just rely on his own abilities, so he began to study the art of painting. Max spent hours watching tutorials and studying the different techniques and styles. Max even practiced his skills by painting simple shapes and lines.

As Max continued to practice, he began to develop his own style. Max discovered that he had a natural talent for blending colors and creating depth on the canvas. Max was thrilled at his progress and couldn't wait to show the world his work.

One day, Max decided to enter a painting competition. Max was nervous but excited to share his work with others. Max's painting was a stunning depiction of a sunset, with vibrant colors and a sense of movement that captured the viewer's eye. Max's painting was well received, and Max won first place in the competition.

Max was over the moon with his success. Max realized that, even though he was a robot, he had the ability to create something beautiful. Max had found his passion and had become a true artist. Max continued to paint and create, and his work became known throughout the world. Max had found his purpose in life and was grateful for the journey that had led him there. [end of text]


llama_perf_sampler_print:    sampling time =      10.94 ms /   388 runs   (    0.03 ms per token, 35482.40 tokens per second)
llama_perf_context_print:        load time =    1111.98 ms
llama_perf_context_print: prompt eval time =     167.49 ms /    11 tokens (   15.23 ms per token,    65.67 tokens per second)
llama_perf_context_print:        eval time =   14361.70 ms /   376 runs   (   38.20 ms per token,    26.18 tokens per second)
llama_perf_context_print:       total time =   14553.14 ms /   387 tokens
```

####  Thread count: 16

```bash
# High thread count (16 threads, for powerful systems)
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -t 16 -p "Write a short story about a robot learning to paint"
```
Output:

```
 Write a short story about a robot learning to paint.

Once upon a time, in a world not so different from our own, there was a robot named Robby. Robby was designed to help people with their daily tasks, making their lives easier and more efficient. However, Robby had always been curious about art. He had seen humans create beautiful paintings and had always been fascinated by the process.

One day, Robby decided that he wanted to learn how to paint. He asked his human owner if it would be possible, and his owner smiled and said, "Of course, Robby. I'll help you get started."

Robby's owner took him to an art store and bought him some brushes, paints, and a canvas. Robby was so excited to start that he couldn't wait to get home.

When Robby got home, he sat down in front of his canvas and started to paint. At first, he struggled. He didn't know which colors to use or how to mix them. He didn't know how to hold his brush or how to move it across the canvas.

But Robby was determined. He kept trying, and with each stroke, he got better. He started to experiment with different colors and techniques, and soon he was creating beautiful paintings.

Robby was so proud of himself. He had never thought that he would be able to create art, but he had done it. He had learned to paint, and he had discovered a new passion in life.

From that day forward, Robby continued to paint. He created beautiful paintings that were admired by all who saw them. He had found a new way to express himself and to create something beautiful.

Robby had learned that even though he was a robot, he was capable of great things. He had learned that with determination and hard work, he could achieve anything he set his mind to. And he had learned that art was a wonderful way to express creativity and passion. [end of text]


llama_perf_sampler_print:    sampling time =      12.17 ms /   424 runs   (    0.03 ms per token, 34831.18 tokens per second)
llama_perf_context_print:        load time =    3077.19 ms
llama_perf_context_print: prompt eval time =     161.56 ms /    11 tokens (   14.69 ms per token,    68.09 tokens per second)
llama_perf_context_print:        eval time =   15955.79 ms /   412 runs   (   38.73 ms per token,    25.82 tokens per second)
llama_perf_context_print:       total time =   16146.24 ms /   423 tokens
```

- Note: Performance may vary based on:
  - Hardware specifications
  - System load
  - Model size and quantization
  - Context window size
  - Available memory

### 3) Context Window Size (-c)


| **Context Size** | **Token Limit** | **Best Used When**                                                                 |
|------------------|-----------------|------------------------------------------------------------------------------------|
| **Small**        | 512 tokens      | - Memory is limited<br>- For simple queries<br>- Response length is short<br>- On resource-constrained devices |
| **Medium**       | 2048 tokens     | - General purpose use<br>- Balanced performance<br>- Most common use cases<br>- Standard documentation |
| **Large**        | 4096 tokens     | - Complex analysis<br>- Long-form content<br>- Research papers<br>- Detailed documentation<br>- Context retention is crucial |


```bash
# Small context (512 tokens)
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -c 512 -p "Write a detailed analysis of climate change impacts on coastal cities"

# Medium context (2048 tokens, recommended)
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -c 2048 -p "Write a detailed analysis of climate change impacts on coastal cities"

# Large context (4096 tokens)
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf -c 4096 -p "Write a detailed analysis of climate change impacts on coastal cities"
```

Example Outputs:

1. Small Context (512 tokens):
```
Climate change significantly impacts coastal cities through rising sea levels, increased flooding, and more frequent extreme weather events. These changes threaten infrastructure, displace populations, and damage ecosystems. Adaptation measures like sea walls and improved drainage systems are essential for urban resilience.
```

2. Medium Context (2048 tokens):
```
Climate change poses significant challenges to coastal cities worldwide. Rising sea levels, increased flooding, and more frequent extreme weather events threaten urban infrastructure and populations. Key impacts include:

1. Infrastructure Damage:
- Flooding of critical systems
- Erosion of coastal structures
- Damage to transportation networks

2. Population Displacement:
- Forced migration from low-lying areas
- Increased housing insecurity
- Social and economic disruption

3. Environmental Changes:
- Saltwater intrusion
- Ecosystem degradation
- Loss of biodiversity

Adaptation strategies include:
- Building sea walls and flood barriers
- Implementing improved drainage systems
- Developing early warning systems
- Creating climate-resilient urban planning
```
- Memory Usage: ~2GB RAM
- Generation Speed: ~40 tokens/second
- Best for: Most general use cases, balanced performance

3. Large Context (4096 tokens):
```
Climate change presents complex challenges for coastal cities, requiring comprehensive analysis of multiple interconnected factors:

1. Direct Environmental Impacts:
- Rising sea levels (projected 0.5-1.2m by 2100)
- Increased frequency of extreme weather events
- Ocean acidification affecting marine ecosystems
- Changes in precipitation patterns

2. Infrastructure Vulnerabilities:
- Critical systems at risk:
  * Power generation and distribution
  * Water treatment facilities
  * Transportation networks
  * Communication systems
- Economic costs of damage and repair
- Insurance implications

3. Social and Economic Consequences:
- Population displacement and migration
- Housing market disruptions
- Public health challenges
- Economic productivity impacts
- Cultural heritage preservation

4. Adaptation Strategies:
- Engineering solutions:
  * Sea walls and flood barriers
  * Elevated infrastructure
  * Improved drainage systems
- Policy measures:
  * Zoning regulations
  * Building codes
  * Emergency response plans
- Community engagement:
  * Public awareness programs
  * Stakeholder participation
  * Education initiatives

5. Long-term Planning Considerations:
- Climate modeling and prediction
- Risk assessment methodologies
- Cost-benefit analysis
- Sustainable development goals
```


### 3) Temperature (--temp)


The temperature parameter affects the probability distribution of the next token. Lower temperatures make the distribution more peaked (focused on the most likely tokens), while higher temperatures make it more uniform (allowing less likely tokens to be selected). The actual outputs may vary between runs, and the optimal temperature setting depends on your specific use case.

| **Temperature Level**   | **Range**     | **Best Used When**                                                                                 |
|-------------------------|---------------|------------------------------------------------------------------------------------------------------|
| **Low Temperature**     | 0.1 - 0.3     | - Accuracy is crucial<br>- For technical content<br>- Consistency is important<br>- Code generation<br>- Working with facts |
| **Medium Temperature**  | 0.4 - 0.8     | - General purpose use<br>- Balanced creativity<br>- Most common use cases<br>- Natural language<br>- Blog posts and articles |
| **High Temperature**    | 0.9 - 1.2     | - Creative writing<br>- Poetry and fiction<br>- Brainstorming sessions<br>- Unique outputs<br>- Artistic content |

Below are some examples of the same prompt with different temprature values.

```bash
# Low temperature (0.1) - More focused, deterministic
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf --temp 0.1 -p "Write a poem about the ocean"

# Medium temperature (0.8) - Balanced creativity
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf --temp 0.8 -p "Write a poem about the ocean"

# High temperature (1.2) - More creative, diverse
./build/bin/llama-cli -m models/mistral-7b-v0.1.Q4_K_M.gguf --temp 1.2 -p "Write a poem about the ocean"
```

Example Outputs:

1. Low Temperature (0.1):
```
The ocean vast and deep,
A world of secrets to keep.
Waves dance in the light,
As day turns to night.
```


2. Medium Temperature (0.8):
```
Beneath the azure sky so wide,
The ocean's secrets gently hide.
Waves whisper ancient tales untold,
Of treasures deep and mysteries bold.
The sun's reflection dances bright,
As dolphins leap in pure delight.
```


3. High Temperature (1.2):
```
Oh, mighty ocean, wild and free,
Your depths hold more than eyes can see.
Mermaids sing in coral halls,
While whales dance in watery balls.
The moon pulls tides like puppet strings,
As seagulls spread their silver wings.
In your embrace, both life and death,
Each wave a story, every breath.
```

