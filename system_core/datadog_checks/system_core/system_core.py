# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import psutil
from six import iteritems

from datadog_checks.base import AgentCheck


class SystemCore(AgentCheck):
    def check(self, instance):
        instance_tags = instance.get('tags', [])

        cpu_times = psutil.cpu_times(percpu=True)
        self.gauge('system.core.count', len(cpu_times), tags=instance_tags)

        for i, cpu in enumerate(cpu_times):
            tags = instance_tags + ['core:{0}'.format(i)]
            for key, value in iteritems(cpu._asdict()):
                self.rate('system.core.{0}'.format(key), 100.0 * value, tags=tags)

        total_cpu_times = psutil.cpu_times()
        n_cpus = psutil.cpu_count()
        for key, value in iteritems(total_cpu_times._asdict()):
            self.rate('system.core.{0}.total'.format(key), 100.0 * value / n_cpus, tags=instance_tags)
