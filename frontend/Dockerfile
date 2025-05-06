FROM node:16-slim

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available) and install dependencies
COPY package.json package-lock.json* /app/
RUN npm install

# Copy the rest of the app
COPY . /app

# Expose the port
EXPOSE 3000

# Set the environment to production (optional, if working on a production app)
ENV NODE_ENV=development

# Run React app
CMD ["npm", "start"]
