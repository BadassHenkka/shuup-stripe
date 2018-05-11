# -*- coding: utf-8 -*-
# This file is part of Shuup Stripe Addon.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import pkg_resources
from shuup.apps import AppConfig

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = None


class ShuupStripeAppConfig(AppConfig):
    name = "shuup_stripe"
    verbose_name = "Shuup Stripe Checkout integration"
    label = "shuup_stripe"

    provides = {
        "front_service_checkout_phase_provider": [
            "shuup_stripe.checkout_phase:StripeCheckoutPhaseProvider",
        ],
        "service_provider_admin_form": [
            "shuup_stripe.admin_forms:StripeCheckoutAdminForm",
        ],
        "payment_processor_wizard_form_def": [
            "shuup_stripe.admin_forms:StripeCheckoutWizardFormDef",
        ],
        "front_urls_pre": [
            "shuup_stripe.urls:urlpatterns"
        ],
        "admin_module": [
            "shuup_stripe.admin_module:StripeAdminModule"
        ]
    }


default_app_config = __name__ + ".ShuupStripeAppConfig"
