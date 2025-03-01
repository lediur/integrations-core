# CHANGELOG - Airflow

## 3.2.0 / 2022-09-16

* [Added] Update HTTP config spec templates. See [#12890](https://github.com/DataDog/integrations-core/pull/12890).

## 3.1.1 / 2022-06-27 / Agent 7.38.0

* [Fixed] Update mapping and tags in README.md. See [#11967](https://github.com/DataDog/integrations-core/pull/11967). Thanks [moshederri](https://github.com/moshederri).
* [Fixed] Update airflow integration dogstatsd_mapper_profiles example. See [#12101](https://github.com/DataDog/integrations-core/pull/12101). Thanks [jessezhang91](https://github.com/jessezhang91).

## 3.1.0 / 2022-04-05 / Agent 7.36.0

* [Added] Add metric_patterns options to filter all metric submission by a list of regexes. See [#11695](https://github.com/DataDog/integrations-core/pull/11695).
* [Fixed] Remove outdated warning in the description for the `tls_ignore_warning` option. See [#11591](https://github.com/DataDog/integrations-core/pull/11591).

## 3.0.0 / 2022-02-19 / Agent 7.35.0

* [Added] Add `pyproject.toml` file. See [#11312](https://github.com/DataDog/integrations-core/pull/11312).
* [Fixed] Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).
* [Changed] Add tls_protocols_allowed option documentation. See [#11251](https://github.com/DataDog/integrations-core/pull/11251).

## 2.1.2 / 2022-01-08 / Agent 7.34.0

* [Fixed] Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).

## 2.1.1 / 2021-11-13 / Agent 7.33.0

* [Fixed] Fix airflow logs example. See [#10475](https://github.com/DataDog/integrations-core/pull/10475).

## 2.1.0 / 2021-10-04 / Agent 7.32.0

* [Added] Add runtime configuration validation. See [#8882](https://github.com/DataDog/integrations-core/pull/8882).
* [Added] Add HTTP option to control the size of streaming responses. See [#10183](https://github.com/DataDog/integrations-core/pull/10183).
* [Added] Add allow_redirect option. See [#10160](https://github.com/DataDog/integrations-core/pull/10160).
* [Fixed] Fix the description of the `allow_redirects` HTTP option. See [#10195](https://github.com/DataDog/integrations-core/pull/10195).

## 2.0.0 / 2021-08-22 / Agent 7.31.0

* [Changed] Remove messages for integrations for OK service checks. See [#9888](https://github.com/DataDog/integrations-core/pull/9888).

## 1.8.0 / 2021-04-19 / Agent 7.28.0

* [Added] Add support for Airflow 2. See [#9064](https://github.com/DataDog/integrations-core/pull/9064).

## 1.7.2 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.7.1 / 2020-12-11 / Agent 7.25.0

* [Fixed] Update check signature. See [#8175](https://github.com/DataDog/integrations-core/pull/8175).

## 1.7.0 / 2020-10-31 / Agent 7.24.0

* [Added] Add ability to dynamically get authentication information. See [#7660](https://github.com/DataDog/integrations-core/pull/7660).
* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).

## 1.6.0 / 2020-09-21 / Agent 7.23.0

* [Added] Add RequestsWrapper option to support UTF-8 for basic auth. See [#7441](https://github.com/DataDog/integrations-core/pull/7441).
* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).
* [Fixed] Update proxy section in conf.yaml. See [#7336](https://github.com/DataDog/integrations-core/pull/7336).

## 1.5.0 / 2020-08-10 / Agent 7.22.0

* [Added] airflow new metrics. See [#7112](https://github.com/DataDog/integrations-core/pull/7112).
* [Fixed] Update logs config service field to optional. See [#7209](https://github.com/DataDog/integrations-core/pull/7209).
* [Fixed] DOCS-838 Template wording. See [#7038](https://github.com/DataDog/integrations-core/pull/7038).
* [Fixed] Update ntlm_domain example. See [#7118](https://github.com/DataDog/integrations-core/pull/7118).
* [Fixed] DOCS-983 Airflow integration. See [#6971](https://github.com/DataDog/integrations-core/pull/6971).

## 1.4.0 / 2020-06-29 / Agent 7.21.0

* [Added] Add note about warning concurrency. See [#6967](https://github.com/DataDog/integrations-core/pull/6967).
* [Fixed] Fix template specs typos. See [#6912](https://github.com/DataDog/integrations-core/pull/6912).

## 1.3.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).
* [Added] Use config spec. See [#6305](https://github.com/DataDog/integrations-core/pull/6305).

## 1.2.0 / 2020-04-04 / Agent 7.19.0

* [Added] Add `ddev test` option to verify support of new metrics. See [#6141](https://github.com/DataDog/integrations-core/pull/6141).
* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).

## 1.1.0 / 2020-02-22 / Agent 7.18.0

* [Added] Add airflow logs. See [#5405](https://github.com/DataDog/integrations-core/pull/5405).

## 1.0.0 / 2020-01-06 / Agent 7.17.0

* [Added] Add Airflow integration. See [#5232](https://github.com/DataDog/integrations-core/pull/5232).

