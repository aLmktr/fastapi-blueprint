FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:0.12.22 /uv /bin/uv

# venv lives outside /app so the compose bind mount doesn't hide it
ENV UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/opt/venv/bin:$PATH"

# DEV=true installs the dev group (used by the compose test service)
ARG DEV=false

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN if [ "$DEV" = "true" ]; then uv sync --frozen; else uv sync --frozen --no-dev; fi

COPY . /app/
EXPOSE 8000
