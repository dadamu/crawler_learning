# Producer Consumer 佐 Rabbitmq

## One Thread Crawler

單執行續任務卡死，效率差。


## Producer Consumer Pattern


###  Definition
![](https://i.imgur.com/ZAv7qjs.png)

1. Create a communication channel for a producer to talk to a consumer. Queues are often used, which I'll tell you more about soon.

2. Create a producer that does some work and keeps sends its resulting data through that communication channel.

3. Create a consumer that keeps reading from that communication channel and processes any data passed to it.


### Multi-thread

利用 Producer Consumer Pattern 概念，建造 Multi-thread 系統讓效率倍增。

### RabbitMQ

一台機器的資源有限，想要將任務分散至各個機子，可使用 RabbitMQ ，並依照各電腦資源分配 Consumer 數量。

```shell=
docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3
```



## Reference


[Finlab 超簡單台股每日爬蟲教學](https://www.finlab.tw/%e8%b6%85%e7%b0%a1%e5%96%ae%e5%8f%b0%e8%82%a1%e6%af%8f%e6%97%a5%e7%88%ac%e8%9f%b2%e6%95%99%e5%ad%b8/)

[RabbitMQ tutorial](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)

[Implement a Producer-Consumer Pattern Using a BlockingQueue](https://openclassrooms.com/en/courses/5684021-scale-up-your-code-with-java-concurrency/6667996-implement-a-producer-consumer-pattern-using-a-blockingqueue)