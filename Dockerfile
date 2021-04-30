# Base Image
FROM python:3

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8001

#======================================
ENV DB_NAME=income_system_db
ENV DB_USER=postgres
ENV DB_PASSWORD=password
ENV DB_HOST=localhost

#=====================================
# Email Config
#=====================================
ENV EMAIL_HOST=smtp.mailtrap.io
ENV EMAIL_PORT=2525
ENV EMAIL_HOST_USER=32331f903778d1
ENV EMAIL_HOST_PASSWORD=df409c5e8264e2
ENV DEFAULT_FROM_EMAIL=noreply@expenses.info

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8001
CMD gunicorn src.wsgi:application --bind 0.0.0.0:$PORT