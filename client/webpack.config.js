const path = require("path");
const webpack = require("webpack");
module.exports = {
  // Where Webpack looks to load your JavaScript
  entry: {
    main: path.resolve(__dirname, "src/index.js"),
  },
  mode: "development",
  // Where Webpack spits out the results (the myapp static folder)
  output: {
    path: path.resolve(__dirname, "../server/mysite/myapp/static/myapp/build/"),
    filename: "[name].js",
    sourceMapFilename: "[name].js.map",
  },
  devtool: "source-map",
  plugins: [
    // Don't output new files if there is an error
    new webpack.NoEmitOnErrorsPlugin(),
  ],
  // Add a rule so Webpack reads JS with Babel
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
    ],
  },

  // Where find modules that can be imported (eg. React)
  resolve: {
    extensions: ["*", ".js", ".jsx"],
    modules: [
      path.resolve(__dirname, "src"),
      path.resolve(__dirname, "src/components"),
      path.resolve(__dirname, "src/components/home"),
      path.resolve(__dirname, "node_modules"),
    ],
  },
};
