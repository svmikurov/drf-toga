==========================================================
Django REST framework project with Toga mobile application
==========================================================

The learn skill project.

Install
~~~~~~~

.. code-block:: console
   :caption: DRF project

   make build

.. code-block:: console
   :caption: Install Toga mobile application development requirements

   sudo apt update
   sudo apt install git build-essential pkg-config python3-dev python3-venv \
   libgirepository1.0-dev libcairo2-dev gir1.2-gtk-3.0 libcanberra-gtk3-module
   pip install -r /toga_app/requirements.txt

.. code-block:: console
   :caption: Development requirements

   pip install -r requirements.dev.txt