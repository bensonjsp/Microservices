FROM golang:latest
WORKDIR /usr/src/app
# Modules
COPY go.mod go.sum ./
RUN go mod download
COPY . .
# Build
RUN go build -o main .
CMD ["./main"]