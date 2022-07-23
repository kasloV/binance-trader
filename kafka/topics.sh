# /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server='kafka:9092' --list

( sleep 5; /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server=kafka:9092 --create --topic=book --config retention.ms=10000 --config segment.ms=10000 ) &
( sleep 5; /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server=kafka:9092 --create --topic=trades --config retention.ms=2400000 --config segment.ms=10000 ) &
