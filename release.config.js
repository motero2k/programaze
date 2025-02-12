module.exports = {
  branches: ['github-actions-CI/CD', 'main'],
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    '@semantic-release/changelog',
    [
      '@semantic-release/exec',
      {
        prepareCmd: 'python setup.py sdist bdist_wheel',
      },
    ],
    [
      '@semantic-release/git',
      {
        assets: ['dist/*', 'CHANGELOG.md', 'package.json'],
        message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}',
      },
    ],
  ],
};
