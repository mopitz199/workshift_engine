docker build -t workshift_engine . && docker run --name workshift_container -it -v $(pwd):/src workshift_engine bash
# docker start workshift_container -i