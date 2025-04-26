<!-- source: https://ui.nuxt.com/components/tooltip --> # Tooltip

[Tooltip](https://reka-
ui.com/docs/components/tooltip)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Tooltip.vue)

A popup that reveals information when hovering over an element.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the Tooltip.

Make sure to wrap your app with the [`App`](/components/app) component which
uses the [`TooltipProvider`](https://reka-
ui.com/docs/components/tooltip#provider) component from Reka UI.

[](/components/app#props)You can check the `App` component `tooltip` prop to
see how to configure the Tooltip globally.

### Text

Use the `text` prop to set the content of the Tooltip.

text

    
    
    <template>
      <UTooltip text="Open on GitHub">
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

### Kbds

Use the `kbds` prop to render [Kbd](/components/kbd) components in the
Tooltip.

    
    
    <template>
      <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

You can use special keys like `meta` that displays as `⌘` on macOS and `Ctrl`
on other platforms.

### Delay

Use the `delay-duration` prop to change the delay before the Tooltip appears.
For example, you can make it appear instantly by setting it to `0`.

delayDuration

    
    
    <template>
      <UTooltip :delay-duration="0" text="Open on GitHub">
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

This can be configured globally through the `tooltip.delayDuration` option in
the [`App`](/components/app) component.

### Content

Use the `content` prop to control how the Tooltip content is rendered, like
its `align` or `side` for example.

content.align

center

content.side

bottom

content.sideOffset

    
    
    <template>
      <UTooltip
        :content="{
          align: 'center',
          side: 'bottom',
          sideOffset: 8
        }"
        text="Open on GitHub"
      >
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

### Arrow

Use the `arrow` prop to display an arrow on the Tooltip.

    
    
    <template>
      <UTooltip arrow text="Open on GitHub">
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

### Disabled

Use the `disabled` prop to disable the Tooltip.

disabled

true

    
    
    <template>
      <UTooltip disabled text="Open on GitHub">
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

## Examples

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    </script>
    
    <template>
      <UTooltip v-model:open="open" text="Open on GitHub">
        <UButton label="Open" color="neutral" variant="subtle" />
      </UTooltip>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the Tooltip by pressing `O`.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`text`| | ` string`The text content of the tooltip.  
`kbds`| | ` (string | undefined)[] | KbdProps[]`The keyboard keys to display in the tooltip.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'kbd'`.
  * `value?: string`
  * `variant?: "outline" | "subtle" | "solid"`Defaults to `'outline'`.
  * `size?: "md" | "sm" | "lg"`Defaults to `'md'`.
  * `class?: any`

  
`content`| `{ side: 'bottom', sideOffset: 8, collisionPadding: 8 }`| `
TooltipContentProps & Partial<EmitsToProps<TooltipContentImplEmits>>`The
content of the tooltip.Show properties

  * `side?: "left" | "right" | "top" | "bottom"`The preferred side of the trigger to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled. Defaults to `"top"`.
  * `sideOffset?: number`The distance in pixels from the trigger. Defaults to `0`.
  * `align?: "center" | "end" | "start"`The preferred alignment against the trigger. May change when collisions occur. Defaults to `"center"`.
  * `alignOffset?: number`An offset in pixels from the `start` or `end` alignment options. Defaults to `0`.
  * `avoidCollisions?: boolean`When `true`, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to `true`.
  * `collisionBoundary?: Element | (Element | null)[] | null`The element used as the collision boundary. By default this is the viewport, though you can provide additional element(s) to be included in this check. Defaults to `[]`.
  * `collisionPadding?: number | Partial<Record<"left" | "right" | "top" | "bottom", number>>`The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { top: 20, left: 20 }. Defaults to `0`.
  * `arrowPadding?: number`The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to `0`.
  * `sticky?: "partial" | "always"`The sticky behavior on the align axis. `partial` will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to `"partial"`.
  * `hideWhenDetached?: boolean`Whether to hide the content when the trigger becomes fully occluded. Defaults to `false`.
  * `positionStrategy?: "fixed" | "absolute"`The type of CSS position property to use.
  * `updatePositionStrategy?: "always" | "optimized"`Strategy to update the position of the floating element on every animation frame. Defaults to `'optimized'`.
  * `forceMount?: boolean`Used to force mounting when more control is needed. Useful when controlling animation with Vue animation libraries.
  * `ariaLabel?: string`By default, screenreaders will announce the content inside the component. If this is not descriptive enough, or you have content that cannot be announced, use aria-label as a more descriptive label. Defaults to `String`.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: Event) => void)`

  
`arrow`| `false`| `boolean | TooltipArrowProps`Display an arrow alongside the tooltip.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the tooltip in a portal.  
`defaultOpen`| | `boolean`The open state of the tooltip when it is initially rendered. Use when you do not need to control its open state.  
`open`| | `boolean`The controlled open state of the tooltip.  
`delayDuration`| `700`| ` number`Override the duration given to the `Provider`
to customise the open delay for a specific tooltip.  
`disableHoverableContent`| | `boolean`Prevents Tooltip.Content from remaining open when hovering. Disabling this has accessibility consequences. Inherits from Tooltip.Provider.  
`disableClosingTrigger`| `false`| `boolean`When `true`, clicking on trigger
will not close the content.  
`disabled`| `false`| `boolean`When `true`, disable tooltip  
`ignoreNonKeyboardFocus`| `false`| `boolean`Prevent the tooltip from opening
if the focus did not come from the keyboard by matching against the `:focus-
visible` selector. This is useful if you want to avoid opening it when
switching browser tabs or closing a dialog.  
`ui`| | ` { content?: ClassNameValue; arrow?: ClassNameValue; text?: ClassNameValue; kbds?: ClassNameValue; kbdsSize?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ open: boolean; }`  
`content`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[value: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        tooltip: {
          slots: {
            content: 'flex items-center gap-1 bg-default text-highlighted shadow-sm rounded-sm ring ring-default h-6 px-2 py-1 text-xs select-none data-[state=delayed-open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-tooltip-content-transform-origin) pointer-events-auto',
            arrow: 'fill-default',
            text: 'truncate',
            kbds: "hidden lg:inline-flex items-center shrink-0 gap-0.5 before:content-['·'] before:me-0.5",
            kbdsSize: 'sm'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            tooltip: {
              slots: {
                content: 'flex items-center gap-1 bg-default text-highlighted shadow-sm rounded-sm ring ring-default h-6 px-2 py-1 text-xs select-none data-[state=delayed-open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-tooltip-content-transform-origin) pointer-events-auto',
                arrow: 'fill-default',
                text: 'truncate',
                kbds: "hidden lg:inline-flex items-center shrink-0 gap-0.5 before:content-['·'] before:me-0.5",
                kbdsSize: 'sm'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            tooltip: {
              slots: {
                content: 'flex items-center gap-1 bg-default text-highlighted shadow-sm rounded-sm ring ring-default h-6 px-2 py-1 text-xs select-none data-[state=delayed-open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-tooltip-content-transform-origin) pointer-events-auto',
                arrow: 'fill-default',
                text: 'truncate',
                kbds: "hidden lg:inline-flex items-center shrink-0 gap-0.5 before:content-['·'] before:me-0.5",
                kbdsSize: 'sm'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ToastA succinct message to provide information or feedback to the
user.](/components/toast)[TreeA tree view component to display and interact
with hierarchical data structures.](/components/tree)

