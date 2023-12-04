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
        '@semantic-release/exec',
        {
          publishCmd: 'twine upload dist/*',
        },
      ],
      '@semantic-release/git',
    ],
  };
  