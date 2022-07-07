# /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server='kafka:9092' --list

( sleep 5; /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server='kafka:9092' --if-not-exists --create --topic='book' ) &
( sleep 5; /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server='kafka:9092' --if-not-exists --create --topic='trades' ) &
