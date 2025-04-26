<!-- source: https://ui.nuxt.com/components/app --> # App

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/App.vue)

Wraps your app to provide global configurations and more.

## Usage

This component implements Reka UI [ConfigProvider](https://reka-
ui.com/docs/utilities/config-provider) to provide global configuration to all
components:

  * Enables all primitives to inherit global reading direction.
  * Enables changing the behavior of scroll body when setting body lock.
  * Much more controls to prevent layout shifts.

It's also using [ToastProvider](https://reka-
ui.com/docs/components/toast#provider) and [TooltipProvider](https://reka-
ui.com/docs/components/tooltip#provider) to provide global toasts and
tooltips, as well as programmatic modals and slideovers.

Use it at the root of your app:

app.vue

    
    
    <template>
      <UApp>
        <NuxtPage />
      </UApp>
    </template>
    

[](/getting-started/i18n/nuxt#locale)Learn how to use the `locale` prop to
change the locale of your app.

[](/getting-started/i18n/vue#locale)Learn how to use the `locale` prop to
change the locale of your app.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`tooltip`| | ` TooltipProviderProps`Show properties

  * `delayDuration?: number`The duration from when the pointer enters the trigger until the tooltip gets opened. Defaults to `700`.
  * `skipDelayDuration?: number`How much time a user has to enter another trigger without incurring a delay again. Defaults to `300`.
  * `disableHoverableContent?: boolean`When `true`, trying to hover the content will result in the tooltip closing as the pointer leaves the trigger. Defaults to `false`.
  * `disableClosingTrigger?: boolean`When `true`, clicking on trigger will not close the content. Defaults to `false`.
  * `disabled?: boolean`When `true`, disable tooltip Defaults to `false`.
  * `ignoreNonKeyboardFocus?: boolean`Prevent the tooltip from opening if the focus did not come from the keyboard by matching against the `:focus-visible` selector. This is useful if you want to avoid opening it when switching browser tabs or closing a dialog. Defaults to `false`.

  
`toaster`| | ` null | ToasterProps`Show properties

  * `position?: "top-left" | "top-center" | "top-right" | "bottom-left" | "bottom-center" | "bottom-right"`The position on the screen to display the toasts. Defaults to `'bottom-right'`.
  * `expand?: boolean`Expand the toasts to show multiple toasts at once. Defaults to `true`.
  * `portal?: string | boolean | HTMLElement`Render the toaster in a portal. Defaults to `true`.
  * `class?: any`
  * `ui?: { viewport?: ClassNameValue; base?: ClassNameValue; }`
  * `label?: string`An author-localized label for each toast. Used to help screen reader users associate the interruption with a toast. Defaults to `'Notification'`.
  * `duration?: number`Time in milliseconds that each toast should remain visible for. Defaults to `5000`.
  * `swipeThreshold?: number`Distance in pixels that the swipe must pass before a close is triggered. Defaults to `50`.

  
`locale`| | ` Locale<Messages>`Show properties

  * `name: string`
  * `code: string`
  * `dir: Direction`
  * `messages: Messages`

  
`portal`| `'body'`| ` string | HTMLElement`  
`scrollBody`| | `boolean | ScrollBodyOption`The global scroll body behavior of your application. This will be inherited by the related primitives.Show properties

  * `padding?: string | number | boolean`
  * `margin?: string | number | boolean`

  
`nonce`| | ` string`The global `nonce` value of your application. This will be inherited by the related primitives.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
[useToastA composable to display toast notifications in your
app.](/composables/use-toast)[AccordionA stacked set of collapsible
panels.](/components/accordion)

