.. _VitalSource:

#########################
VitalSource E-Reader Tool
#########################

The VitalSource Bookshelf e-reader tool provides your students with easy access to electronic books. Students can not only read text, but also quickly browse and search content (including figures and notes), create and manage notes and multiple highlighters, and copy notes into external documents.

.. image:: /Images/VitalSource.png
   :width: 500
   :alt: VitalSource e-book with highlighted note

For more information about Vital Source and its features, visit the `VitalSource Bookshelf support site <https://support.vitalsource.com/hc/en-us>`_.

.. note:: Before you add a VitalSource Bookshelf e-reader to your course, you must work with Vital Source to make sure the content you need already exists in the Vital Source inventory. If the content is not yet available, Vital Source works with the publisher of the e-book to obtain files that meet the VitalSource Bookshelf specifications. This process can take up to four months. The following steps assume that the e-book you want is already part of the Vital Source inventory.

**************************
Add a VitalSource E-Reader
**************************

Adding a VitalSource Bookshelf e-reader has several steps:

#. :ref:`Modify the course's advanced settings to allow you to create a Vital Source Learning Tools Interoperability (LTI) component<VS Modify Advanced Settings>`.

#. :ref:`Add the VitalSource Bookshelf e-reader to a unit<VS Add VS EReader>`.


.. _VS Modify Advanced Settings:

=============================================
Step 1. Modify the Course's Advanced Settings
=============================================

#. Obtain the value for the **lti_passports** policy key and the Vital Souce Book ID (VBID) for your e-book from your Vital Source account manager.

#. In Studio, click the **Settings** menu, and then click **Advanced Settings**.

#. On the **Advanced Settings** page, locate the **advanced_modules** policy key.

#. Under **Policy Value**, place your cursor between the brackets, and then enter ``“lti”``. Make sure to include the quotation marks, but not the period.

   .. image:: /Images/LTIPolicyKey.png
    :alt: Image of the advanced_modules key in the Advanced Settings page, with the LTI value added

   **Note** If the **Policy Value** field already contains text, place your cursor directly after the closing quotation mark for the final item, and then enter a comma followed by ``“lti”`` (make sure that you include the quotation marks). For example, the text in the **Policy Value** field may resemble the following:

   ``["value_1","lti"]``

4. Scroll down to the **lti_passports** policy key.

#. Under **Policy Value**, place your cursor between the brackets, and then enter the value for the **lti_passports** policy key that you obtained from your VitalSource account manager.

#. At the bottom of the page, click **Save Changes**.

The page refreshes automatically. At the top of the page, you see a notification that your changes have been saved.

.. _VS Add VS EReader:

==============================================================
Step 3. Add the VitalSource Bookshelf E-Reader to a Unit
==============================================================

To add the VitalSource Bookshelf e-reader to a unit, you'll create an LTI component, and then configure several settings in the component.

#. In the unit where you want to create the problem, click **Advanced** under **Add New Component**, and then click **LTI**.

#. In the component that appears, click **Edit**.

#. In the **Display Name** field, type the name of your e-book. This name appears at the top of the component and in the course ribbon at the top of the page in the courseware.

#. Next to **Custom Parameters**, click **Add**.

#. In the field that appears, enter the following (where ``VitalSourceCode`` is the code for the e-book that you received from Vital Source):

   ``vbid=VitalSourceCode``

   If you want to test an e-book in your course, but you don't yet have the code for the e-book, you can enter ``vbid=L-999-70103`` to create a link to *Pride and Prejudice*.

#. If you want your e-book to open to a specific page, click **Add** next to **Custom Parameters** again, and then add the following (where ``35`` is the page of the e-book):

   ``book_location=page/35``

#. In the **Launch URL** field, enter the following (make sure to use ``https`` instead of ``http``):

  ``https://bc.vitalsource.com/books/book``

8. In the **LTI ID** field, enter the following:

  ``vital_source``

9. Click **Save**.

**************************
Information for Students
**************************

Each institution's Vital Source account manager will train the MPP on the VitalSource Bookshelf e-reader and provide supporting documentation as part of the onboarding process. However, to improve the learner experience, we recommend that you provide the following explanation of the e-reader to your students:

Using a digital textbook in the VitalSource Bookshelf e-reader has several benefits: Simple, user-friendly navigation; easy, intuitive access; and instant access to content. Below is a list of the VitalSource Bookshelf e-reader features that you will use most often during the course:

* Browse content, figures, and notes and filter search results.
* Create and manage multiple highlighters.
* Create and manage notes.
* Copy and paste notes into external documents.

For more information about how to use these features, visit the `VitalSource Bookshelf support site <https://support.vitalsource.com>`_.

