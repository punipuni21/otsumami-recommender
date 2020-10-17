const path = require("path");

module.exports = {
  output: {
    path: path.resolve(
      __dirname,
      "project/frontend/static/frontend"
    ),
    filename: "main.js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  /* webpack-dev-server 用*/
  entry: {
    index: path.join(__dirname, "project", "frontend", "src", "index.js"),
  },
  devServer: {
    open: true,
    contentBase: path.join(__dirname, "project/frontend/templates/frontend"),
    openPage: "index.html",
    port: 3000,
    compress: true,
    watchContentBase: true,
    historyApiFallback: true,
  }
};
