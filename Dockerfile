FROM python:3.9.2

RUN apt-get update && apt-get install -y unzip

# install google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# install pipenv
RUN pip install pipenv

# install ChromeDriver
ADD  https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

COPY . .

ENV PIPENV_VENV_IN_PROJECT true
RUN pipenv --rm && pipenv install

CMD [ "pipenv", "run", "python", "amazon.py" ]
