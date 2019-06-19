# Use python script to sort our input by hugo's weight system.
FROM python:3-alpine as sorting
WORKDIR /src
COPY ./scripts/epub/ ./
COPY ./content/ ./content
RUN pip install -r requirements.txt && \
	python sortcontent.py

# Use pandoc to create our epub.
FROM pandoc/core:2.7 as transpiling
WORKDIR /src
COPY --from=sorting /src/order.txt ./
COPY ./content/ ./content
RUN pandoc -o sfosc.epub `cat order.txt`

# Store results in a fresh container.
FROM busybox
WORKDIR /dist
COPY --from=transpiling /src/sfosc.epub ./
