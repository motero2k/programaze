module.exports = {
  branches: ['github-actions-CI/CD', 'main'],
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    '@semantic-release/changelog',
    '@semantic-release/git',
  ],
};
