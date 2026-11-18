# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

## Adding

- Updating new changes for next version

## [v7]

### Added - Todo endpoint authentication

- Allow only owner of the todo to make crud operations based on user authentication
- Checked todos routes authentication on the swagger docs

## [v6]

### Added - Authentication

- Added user model connecting to specific todos records
- Added signin route to create user with hashed password
- Added login route to authenticate user
- Added get current user route to verify the token generated to get user details
- Checked all routes on the swagger docs

## [v5]

### Restructuring - Add support for multiple router files

- Have separate file for todo api router file
- Include them into main file so that the main file could support multiple router files
- Retest the code with inbuilt swagger docs

## [v4]

### Added - Added Changelog

- Added version tags
- Added Changelog docs connecting to the tags

## [v3]

### Added - Added todo CRUD

- Connect to sqlite database
- Create todo model
- Crud operation added for todo with pydantic
- Tested with swagger docs
- App running command [uvicorn main:app --reload]

## [v2]

### Added - Added package requirement

- Added requirements.txt which contains package required info.
- Added basic README file

## [v1] - Started Working

### Added

- Initial Commit

[unreleased]: https://github.com/deepak0023/fastapi/compare/v7...HEAD
[v7]: https://github.com/deepak0023/fastapi/compare/v6...v7
[v6]: https://github.com/deepak0023/fastapi/compare/v5...v6
[v5]: https://github.com/deepak0023/fastapi/compare/v4...v5
[v4]: https://github.com/deepak0023/fastapi/compare/v3...v4
[v3]: https://github.com/deepak0023/fastapi/compare/v2...v3
[v2]: https://github.com/deepak0023/fastapi/compare/v1...v2
[v1]: https://github.com/deepak0023/fastapi/releases/tag/v1
