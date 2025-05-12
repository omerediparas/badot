FROM node:18-slim

# Set working directory
WORKDIR /app

# Copy only package.json and install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Use development mode for hot reload
ENV NODE_ENV=development

# Start the app
CMD ["npm", "start"]
